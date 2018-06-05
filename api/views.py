from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import views
from rest_framework.permissions import IsAuthenticated

from api.serializers import UserSerializer


class EchoView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({'users': serializer.data})
