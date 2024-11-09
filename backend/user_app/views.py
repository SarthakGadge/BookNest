from django.shortcuts import render
from .serializers import UserDetailsSerializer
from .models import UserDetails
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class UserView(APIView):
    def post(self, request):
        if request.user.role == 'user':
            return Response({"msg": "You are unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        id = request.user.id
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        serializer = UserDetailsSerializer
        if pk:
            if request.user.role == 'user':
                id = request.user.id
                user = get_object_or_404(UserDetails, pk=pk)
                serializer = UserDetailsSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "You are unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            if not request.user.role == 'admin':
                return Response({"msg": "You are unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
            users = UserDetails.objects.all()
            serializer = UserDetailsSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
