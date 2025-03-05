from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from pf_users.models import User


class PasswordReset:
    def __init__(self, email=None, scheme=None, host=None , uidb64=None, token=None, new_password=None):
        self.email = email
        self.scheme = scheme
        self.host = host
        self.uidb64 = uidb64
        self.token = token
        self.new_password = new_password

    def send_reset_email(self):
        try:
            user = User.objects.get(email=self.email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"{self.scheme}://{self.host}/api/reset-password/{uid}/{token}/"
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_link}',
                'from@example.com',
                [self.email],
                fail_silently=False,
            )
            return Response({"message": "Password reset link sent."}, status=200)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=400)

    def reset_password(self):
        try:
            uid = urlsafe_base64_decode(self.uidb64).decode()
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, self.token):
                user.set_password(self.new_password)
                user.save()
                return Response({"message": "Password has been reset."}, status=201)
            else:
                return Response({"error": "Invalid token."}, status=400)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error": "Invalid request."}, status=400)
