# from django.urls import path
from rest_framework.routers import DefaultRouter

from publisher_api.views.v1 import PublisherViewSet


router = DefaultRouter()


router.register('', PublisherViewSet, basename='publishers')


urlpatterns = []

urlpatterns += router.urls
