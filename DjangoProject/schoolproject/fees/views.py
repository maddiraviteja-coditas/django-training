from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def fees_django(request):
    return HttpResponse("Hi welcome to django Fees..")


def fees_python(request):
    return HttpResponse("Hi welcome to Python Fees..")


def fees_react(request):
    return HttpResponse("Hi welcome to react Fees..")


def calculate_fees(request):
    result = 10 + 20
    return HttpResponse(f"hey the fees is: {result}")


