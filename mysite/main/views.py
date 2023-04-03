from django.urls import path
from django.shortcuts import render



app_name = 'main'
def index(request):
    msg = 'hi'
    return render(request, 'main/main.html',{'message': msg})