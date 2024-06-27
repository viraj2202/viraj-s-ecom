from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.order import api

router = DefaultRouter()
router.register(r'orders', api.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
