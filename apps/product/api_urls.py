from django.urls import path,include
from . import api
from rest_framework.routers import DefaultRouter
# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'products', api.ProductViewSet)
router.register(r'categories', api.CategoryViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]

