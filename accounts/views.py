from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, world.")

def products(request):
    return HttpResponse("Product page.")


def customers(request):
    return HttpResponse("Customer page.")
