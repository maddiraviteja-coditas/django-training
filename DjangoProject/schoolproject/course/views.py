from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def learn_django(request):
    return HttpResponse("Hi welcome to django..")


def learn_python(request):
    return HttpResponse("Hi welcome to Python..")


def learn_react(request):
    return HttpResponse("Hi welcome to react..")


def math_operation(request):
    result = 10 + 20
    return HttpResponse(f"hey the result is: {result}")


