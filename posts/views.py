from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    stuff = {}
    return render(request, 'posts/base.html')
