from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from pf_users.models import User
from pf_users.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

    @swagger_auto_schema(
        operation_description="Retrieve a list of all users",
        responses={
            200: openapi.Response(
                description="List of users",
                examples={
                    'application/json': [
                        {
                            'id': 1,
                            'username': 'defaultuser1',
                            'email': 'defaultuser1@example.com',
                            'first_name': 'Default',
                            'last_name': 'User1',
                            'detail_user': 'http://localhost:8000/api/users/1/'
                        },
                        {
                            'id': 2,
                            'username': 'defaultuser2',
                            'email': 'defaultuser2@example.com',
                            'first_name': 'Default',
                            'last_name': 'User2',
                            'detail_user': 'http://localhost:8000/api/users/2/'
                        }
                    ]
                }
            ),
            401: 'Unauthorized'
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve a user by ID",
        responses={
            200: openapi.Response(
                description="User details",
                examples={
                    'application/json': {
                        'id': 1,
                        'username': 'defaultuser',
                        'email': 'defaultuser@example.com',
                        'first_name': 'Default',
                        'last_name': 'User',
                        'detail_user': 'http://localhost:8000/api/users/1/'
                    }
                }
            ),
            401: 'Unauthorized',
            404: 'User not found'
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update account of authenticated user",
        responses={
            200: openapi.Response(
                description="Update successful",
                examples={
                    'application/json': {
                        'id': 1,
                        'username': 'defaultuser',
                        'email': 'defaultuser@example.com',
                        'first_name': 'Default',
                        'last_name': 'User'
                    }
                }
            ),
            401: 'Unauthorized',
            403: 'Only can update your own account'
        },
        examples={
            'application/json': {
                'username': 'defaultuser',
                'email': 'defaultuser@example.com',
                'password': 'defaultpassword'
            }
        }
    )
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user != user:
            return Response({"error": "Only can update your own account"}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partially update account of authenticated user",
        responses={
            200: openapi.Response(
                description="Partial update successful",
                examples={
                    'application/json': {
                        'id': 1,
                        'username': 'defaultuser',
                        'email': 'defaultuser@example.com',
                        'first_name': 'Default',
                        'last_name': 'User'
                    }
                }
            ),

            401: 'Unauthorized',
            403: 'Only can partially update your own account'
        },
        examples={
            'application/json': {
                'username': 'defaultuser',
                'email': 'defaultuser@example.com',
                'password': 'defaultpassword'
            }
        }
    )
    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user != user:
            return Response({"error": "Only can partially update your own account"}, status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete account of authenticated user",
        responses={
            204: openapi.Response(
                description="Delete successful",
                examples={
                    'application/json': {
                        'detail': 'Account deleted successfully'
                    }
                }
            ),
            401: 'Unauthorized',
            403: 'Only can delete your own account'
        },
        examples={
            'application/json': {
                'username': 'defaultuser',
                'email': 'defaultuser@example.com',
                'password': 'defaultpassword'
            }
        }
    )
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user != user:
            return Response({"error": "Only can delete your own account"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)