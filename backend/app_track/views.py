from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework import generics
from rest_framework.response import Response

from .serializer import *
from .models import *

# Create your views here.

class PersonneList(generics.ListCreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer

@api_view(['GET'])
def all_personne(request):
    tasks = Personne.objects.all()
    serializer = PersonneSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_personne(request):
    data = request.data
    serializer = PersonneSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
