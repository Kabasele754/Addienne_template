from rest_framework import serializers
from .models import *

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = ['name',]