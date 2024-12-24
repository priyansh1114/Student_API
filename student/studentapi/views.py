from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import studenapi
from .serilizer import studentSerializer


def home(request):
    return HttpResponse("studentapi is working as expected")
# Create your views here.


class students(viewsets.ModelViewSet):
    queryset = studenapi.objects.all()
    serializer_class = studentSerializer
