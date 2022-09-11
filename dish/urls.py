from django.urls import path
from rest_framework import routers

from dish.api import IsPublishViewSet

router = routers.DefaultRouter()

api_urls = [
    path(r'foods', IsPublishViewSet.as_view(), name='is_publish'),
]
