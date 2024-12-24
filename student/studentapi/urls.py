from django.contrib import admin
from django.urls import path , include
from .views import home,students
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', students, basename='student')

urlpatterns = [
  path("", home , name = "home"),
  path("", include(router.urls))
  
]