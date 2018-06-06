from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import UserSerializer, UserDetailSerializer


class EchoView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': 'create error'}, status=status.HTTP_204_NO_CONTENT)


class UserDetail(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = UserDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})
