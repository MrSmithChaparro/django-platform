from rest_framework import serializers
from pf_users.models import User

class UserSerializer(serializers.ModelSerializer):
    detail_user = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'full_name',
            'password',
            'is_active',
            'detail_user'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_detail_user(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/users/{obj.id}/')