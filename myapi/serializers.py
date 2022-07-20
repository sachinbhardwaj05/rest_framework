from dataclasses import field
from rest_framework import serializers
from .models import Tufankadevta
class tufanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tufankadevta
        fields=['id','title','description']
