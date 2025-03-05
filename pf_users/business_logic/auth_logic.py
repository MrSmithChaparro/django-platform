from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class AuthLogic:

    def __init__(self, request, email, password):
        self.request = request
        self.email=email
        self.password=password

    def login(self):
        user = authenticate(self.request, email=self.email, password=self.password)
        if user is not None and user.is_active:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials or inactive user'}, status=status.HTTP_401_UNAUTHORIZED)
