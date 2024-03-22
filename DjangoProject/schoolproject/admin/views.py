from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def admin_django(request):
    return HttpResponse("Hi welcome to django Admin..")


def admin_python(request):
    return HttpResponse("Hi welcome to Python Admin..")


def admin_react(request):
    return HttpResponse("Hi welcome to react Admin..")



