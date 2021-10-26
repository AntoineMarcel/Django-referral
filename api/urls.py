# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from .views import Parrains, CreateParrains

urlpatterns = [
    path('parrains/', Parrains.as_view()),
    path('parrains/<str:campaignToken>/<str:userCode>', Parrains.as_view()),
    path('create_parrains/', CreateParrains.as_view())
]