from ast import Delete
from rest_framework import status
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import tufanSerializer
from .models import Tufankadevta
from rest_framework.decorators import api_view

from myapi import serializers
# Create your views here.
@api_view(['GET','POST'])
def tufankilist(request):
    # first step get data from our model
    if request.method=='GET':
        devta=Tufankadevta.objects.all()

    # second step serialize them
        serializer=tufanSerializer(devta,many=True)
    #return json
        return JsonResponse(serializer.data,safe=False)

    if request.method=='POST':
        serializer=tufanSerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def tufankebareme(request,pk):
    try:
        devta=Tufankadevta.objects.get(id=pk)
    except devta.Doesnotexist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers=tufanSerializer(devta)
        return Response(serializers.data)

    if request.method=='PUT':
        serializers=tufanSerializer(devta,request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        devta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)