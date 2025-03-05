from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from pf_users.business_logic.password_reset import PasswordReset
from pf_users.serializers.pasword_reset import PasswordResetSerializer


class PasswordResetView(APIView):
    name = 'password-reset'
    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer

    @swagger_auto_schema(
        request_body=serializer_class,
        operation_description="Request a password reset",
        responses={
            201: 'password has been reset',
            400: 'invalid request or token'
        },
        examples={
            'application/json': {
                'new_password': 'password'
            }
        }
    )
    def post(self, request, uidb64, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        reset_password = PasswordReset(
            uidb64=uidb64,
            token=token,
            new_password=serializer.validated_data.get('new_password')
        )

        return reset_password.reset_password()
