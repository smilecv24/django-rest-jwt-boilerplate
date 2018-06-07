from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import UserSerializer, UserDetailSerializer, UserCreateSerializer


class EchoView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserCreateSerializer

    def get(self, request):
        """
        Get all users
        """
        users = User.objects.all().order_by('id')
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        """
        Add user
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': 'create error'}, status=status.HTTP_204_NO_CONTENT)


class UserDetail(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        """
        Update user by ID
        """
        snippet = self.get_user(pk)
        serializer = UserDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
        users = User.objects.all().order_by('id')
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def delete(self, request, pk):
        """
        Delete user by ID
        """
        snippet = self.get_user(pk)
        snippet.delete()
        users = User.objects.all().order_by('id')
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})
