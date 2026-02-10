from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Product, Order, Customer


# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    ps = Product.objects.all()
    return render(request, 'accounts/products.html', {'ps': ps})


def customer(request):
    return render(request, 'accounts/customer.html')
