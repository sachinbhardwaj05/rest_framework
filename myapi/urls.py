from myapi import views
from django.contrib import admin
from django.urls import path,include
from myapi import urls

urlpatterns = [
    path('myapi/',views.tufankilist)
    path('myapi/<int:pk>/',views.tufankebareme)

]