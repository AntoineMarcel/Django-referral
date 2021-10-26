# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from .views import Parrains, CreateParrains

# router = routers.DefaultRouter()
# router.register(r'parrains', views.ParrainViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('parrains/<str:campaignToken>/<str:userCode>', Parrains.as_view()),
    path('create_parrains', CreateParrains.as_view())
]