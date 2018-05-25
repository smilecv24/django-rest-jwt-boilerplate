from django.http import JsonResponse
from rest_framework import views
from rest_framework.permissions import IsAuthenticated


class EchoView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return JsonResponse({'test': 'test'})
