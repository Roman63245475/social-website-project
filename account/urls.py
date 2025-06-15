from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

# path('login/', user_login, name='login')
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
]
