from django.shortcuts import render

# Create your views here.
# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')