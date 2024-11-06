from rest_framework import serializers

from user_api.models import User


class UserSerializer(serializers.ModelSerializer):
    role_display = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'password',
            'first_name', 'middle_name', 'last_name',
            'full_name', 'role', 'role_display', 'profile_image',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_role_display(self, obj):
        return obj.get_role_display()

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data.get('username', None),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', None),
            middle_name=validated_data.get('middle_name', None),
            last_name=validated_data.get('last_name', None),
        )

        return user
