from django.urls import path
from .views import *
from django.conf import settings
urlpatterns = [
    path('',Home_page,name="home"),
    path('success/', SuccessView, name="success"),
]