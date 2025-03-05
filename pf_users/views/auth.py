from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from pf_users.business_logic.auth_logic import AuthLogic
from pf_users.serializers.auth import LoginSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]
    name = 'login'

    @swagger_auto_schema(
        request_body=LoginSerializer,
        operation_description="Login with email and password",
        responses={200: 'Login successful', 400: 'Invalid input', 401: 'Invalid credentials or inactive user'},
        examples={
            'application/json': {
                'email': 'defaultuser@example.com',
                'password': 'defaultpassword'
            }
        },

    )
    def post(self, request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        response = AuthLogic(request, email=email, password=password)

        return response.login()
