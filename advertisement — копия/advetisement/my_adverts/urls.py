from django.urls import path
from .views import *

urlpatterns = [
    path('main_page', index, name='main_page'),
    path('top-sellers', topSellers, name='top-sellers'),
    path('register', Register, name='register'),
    path('login', Login, name='login'),
    path('profile', Profile, name='profile'),
]