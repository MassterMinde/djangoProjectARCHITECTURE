from abc import ABC

from rest_framework import serializers


class URLSerializer(serializers.Serializer, ABC):
    input_URL = serializers.StringRelatedField()
    output = serializers.StringRelatedField()
