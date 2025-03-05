from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        help_text="email of user"
    )
    password = serializers.CharField(
        required=True,
        help_text="password of user"
    )