from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import permissions
from .permissions import IsOwner


class BlogListAPIView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Blog.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)