from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def Home(request):
    return HttpResponse("Hi welcome Home..")