from rest_framework import serializers

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        help_text="Email of the user requesting password reset"
    )