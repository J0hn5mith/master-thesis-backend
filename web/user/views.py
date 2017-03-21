from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .serializers import UserSerializer, UserConfigurationSerializer
from .models import UserConfiguration


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserConfigurationViewSet(viewsets.ModelViewSet):
    queryset = UserConfiguration.objects.all()
    serializer_class = UserConfigurationSerializer


@api_view(['GET'])
def currentUser(request):
    user = request.user
    if user.is_authenticated:
        user_serializer = UserSerializer(
            user, context={'request': Request(request)}
        )
        return Response(user_serializer.data)
    else:
        return Response(
            data={'error': 'Not allowed if not logged in'},
            status=status.HTTP_401_UNAUTHORIZED,
        )
