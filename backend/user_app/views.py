from django.shortcuts import render
from .serializers import UserDetailsSerializer
from .models import UserDetails
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import UserDetails
from userauth.models import CustomUser


class UserView(APIView):
    def post(self, request):
        # Ensure the user is authorized (only users with role 'user' are allowed)
        if request.user.role != 'user':
            return Response({"msg": "You are unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        # Get the current user's ID from the JWT token (request.user.id)
        user_id = request.user.id

        # Check if UserDetails already exists for this user
        if UserDetails.objects.filter(user_id=user_id).exists():
            return Response({"msg": "User details already exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Modify the incoming request data to add the 'user' field before serializing
        request.data['user'] = request.user.id

        # Serialize the request data
        serializer = UserDetailsSerializer(data=request.data)

        if serializer.is_valid():
            # Save the instance without explicitly setting the 'user' field here
            serializer.save()

            # Return the created data in the response
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = UserDetailsSerializer
        if request.user.role == 'user':
            id = request.user.id
            user = get_object_or_404(UserDetails, user_id=id)
            serializer = UserDetailsSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.user.role == 'admin':
            users = UserDetails.objects.all()
            serializer = UserDetailsSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg": "You are unauthorized"}, sjtatus=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        user_id = request.user.id
        user_instance = get_object_or_404(UserDetails, user_id=user_id)

        serializer = UserDetailsSerializer(
            user_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Changes have been saved",
                             "data": serializer.data
                             }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
