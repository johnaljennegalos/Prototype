from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Product


# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    ps = Product.objects.all()
    return render(request, 'accounts/products.html', {'ps': ps})


def customer(request):
    return render(request, 'accounts/customer.html')
