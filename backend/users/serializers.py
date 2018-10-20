from rest_framework import serializers

# from .models import User


class UserSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=128)
    lastName = serializers.CharField(max_length=128)
    userType = serializers.CharField(max_length=128)

