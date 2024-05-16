from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters, pagination
from . import models
from . import serializers

class PostViewset(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.ServiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__email', 'contant','category']

class ReviewViewset(viewsets.ModelViewSet):
    
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer