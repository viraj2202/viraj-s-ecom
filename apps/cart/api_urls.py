from django.urls import path,include
from . import api
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'cart', api.CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

