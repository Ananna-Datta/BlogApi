from rest_framework import serializers
from . import models

class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    category = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Post
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'