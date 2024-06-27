from django.urls import path
from . import api

urlpatterns = [
    path('register/', api.RegisterView.as_view(), name='register'),
    path('login/', api.LoginAPIView.as_view(), name='login'),
    path('logout/', api.LogoutView.as_view(), name='logout'),
]