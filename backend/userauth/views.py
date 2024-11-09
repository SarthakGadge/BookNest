from .utils import send_email, forgot_password_email
import random
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login
import jwt
from django.conf import settings


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        required_fields = ['username', 'email', 'password']

        for field in required_fields:
            if not request.data.get(field):
                return Response({'msg': f'{field.capitalize()} is required'}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=username).exists():
            return Response({'msg': 'Username already in use.'}, status=400)

        if len(password) < 8:
            return Response({'msg': 'Password must be at least 8 characters long.'}, status=400)

        if CustomUser.objects.filter(email=email).exists():
            return Response({'msg': 'Email already in use.'})

        user = CustomUser.objects.create_user(
            username=username, email=email, password=password, role='user')
        user.is_active = False  # Deactivate account until email is verified
        user.save()

        if send_email(user):
            return Response({'msg': "Verify your email to complete registration. OTP sent for account activation"})
        else:
            return Response({"msg": "Error sending OTP. Please try again later."})


class VerifyOTP(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        # Find the user based on the provided email
        user = CustomUser.objects.filter(email=email).first()
        if not user:
            return Response({'msg': "User with this email not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is already verified
        if user.is_active:
            return Response({'msg': "Account is already verified."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the OTP and expiration
        if user.otp == otp:
            # Check OTP expiration
            if user.is_otp_valid():
                # Activate the user and reset OTP-related fields
                user.is_active = True
                user.otp = None
                user.max_otp_try = 5
                user.otp_expiry = None
                user.otp_max_out = None
                user.save()

                # Issue JWT tokens
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "msg": "You have successfully verified your email."
                }, status=status.HTTP_200_OK)
            else:
                # OTP has expired
                return Response({'msg': "OTP has expired. Please request a new one."}, status=status.HTTP_400_BAD_REQUEST)

        # Invalid OTP case
        return Response({'msg': "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = CustomUser.objects.filter(email=email).first()

        if not user:
            return Response({"msg": "There is no user registered with this email."}, status=status.HTTP_400_BAD_REQUEST)

        if user.is_active == 'false':
            if send_email(user):
                return Response({"msg": "The email registered with this account has not been verified, an otp has been sent to your email. Please verify your email."}, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "We tried sending an OTP to your account. But, an error occurred. Please try again later."}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        authenticated_user = authenticate(
            request, email=email, password=password)
        if authenticated_user:
            login(request, authenticated_user)
            refresh = RefreshToken.for_user(authenticated_user)

            payload = {
                'user_id': authenticated_user.id,
                'username': authenticated_user.username,
                'email': authenticated_user.email,
                'role': authenticated_user.role
            }
            jwt_token = jwt.encode(
                payload, settings.SECRET_KEY, algorithm='HS256')

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'jwt_token': jwt_token,  # Include the JWT token in the response
                'username': authenticated_user.username,
                'email': authenticated_user.email,
                'role': authenticated_user.role,
            }, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        email = request.user.email
        role = request.user.role
        username = request.user.username
        data = {
            'email': email,
            'role': role,
            'username': username
        }
        return Response(data)


class ForgotPasswordRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
            otp = str(random.randint(1000, 9999))
            user.password_reset_otp = otp
            user.password_reset_otp_expiry = timezone.now() + timezone.timedelta(minutes=10)
            user.save()

            forgot_password_email(user, otp, purpose="password reset")

            return Response({"message": "Password reset OTP sent to your email"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)


class ForgotPasswordVerifyView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        new_password = request.data.get('new_password')

        if not all([email, otp, new_password]):
            return Response({"error": "Email, OTP, and new password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)

            if user.password_reset_otp == otp and user.password_reset_otp_expiry > timezone.now():
                # OTP is valid, reset the password
                user.set_password(new_password)
                user.password_reset_otp = None
                user.password_reset_otp_expiry = None
                user.save()

                return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid or expired OTP"}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)


User = get_user_model()


class ResendOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            # print(user.username)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user's account is already active
        if user.is_active == 1:
            return Response({"error": "This account is already active"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            send_email(user=user)
            return Response({"msg": "Your email address has not been verified. An OTP has been sent to your email for account activation"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": "Problem while sending OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
