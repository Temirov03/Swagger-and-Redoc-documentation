from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer
from .models import Blog



class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Create your views here.
