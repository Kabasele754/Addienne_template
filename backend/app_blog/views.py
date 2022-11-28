from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import permissions
from .permissions import IsOwner


class BlogListAPIView(ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Blog.objects.all()
    #lookup_field = "id"

    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)
    
# Get All the data, Create data with Post
class BlogViewSet(APIView):# generics.GenericAPIView
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
    def get(self, request, format=None):
        transformers = Blog.objects.all()
        serializer = BlogSerializer(transformers, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Retrieve, update or delete a Drinks instance
class BlogDetail(APIView):
    """
    Retrieve, update or delete a Drinks instance
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = BlogSerializer(transformer)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = BlogSerializer(transformer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        transformer = self.get_object(pk)
        serializer = BlogSerializer(transformer,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    