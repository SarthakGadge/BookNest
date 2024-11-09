from django.urls import path, include
from .views import ForgotPasswordRequestView, ForgotPasswordVerifyView, RegisterView, LoginView, ResendOTPView, UserProfileView, VerifyOTP


urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("verify_otp/", VerifyOTP.as_view(), name="verify_otp"),
    path('forgot-password/', ForgotPasswordRequestView.as_view(),
         name='forgot-password-request'),
    path('reset-password/', ForgotPasswordVerifyView.as_view(),
         name='forgot-password-verify'),
    path('current_user/', UserProfileView.as_view(), name='user-profile'),
    path('resend_otp/', ResendOTPView.as_view(), name='resend-otp'),
]
