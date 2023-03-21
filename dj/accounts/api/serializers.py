from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    # confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # , 'confirm_password']

    # def validate(self, attrs):
    #     attrs = super().validate(attrs)
    #     if attrs.get('password') != attrs.get('confirm_password'):
    #         raise serializers.ValidationError({'confirm_password': 'Password Must match'})
    #     return attrs

    def create(self, validated_data):
        # validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
