from rest_framework import serializers

class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        help_text="New password for the user"
    )
