from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Product, Order, Customer


# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    context = {'orders': orders, 'customers': customers}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    ps = Product.objects.all()
    return render(request, 'accounts/products.html', {'ps': ps})


def customer(request):
    return render(request, 'accounts/customer.html')
