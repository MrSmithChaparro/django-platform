from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from pf_users.business_logic.password_reset import PasswordReset
from pf_users.serializers.password_reset_request import PasswordResetRequestSerializer


class PasswordResetRequestView(APIView):
    name = 'password-reset-request'
    permission_classes = [AllowAny]
    serializer_class = PasswordResetRequestSerializer

    @swagger_auto_schema(
        request_body=serializer_class,
        operation_description="Request a password reset",
        responses={
            200: 'send email with reset link',
            400: 'email does not exist'
        },
        examples={
            'application/json': {
                'email': 'user@example.com'
            }
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')

        send_mail = PasswordReset(email=email,scheme=request.scheme, host=request.get_host())
        return send_mail.send_reset_email()
