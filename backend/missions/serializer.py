from rest_framework import serializers


class MissionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=512)

