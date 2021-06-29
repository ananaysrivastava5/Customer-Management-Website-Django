from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
    orders_pending = Order.objects.filter(status='Pending').count()
    orders_delivered = Order.objects.filter(status='Delivered').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'orders_pending': orders_pending,
        'orders_delivered': orders_delivered,
    }

    return render(request,'accounts/dashboard.html', context)



def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'accounts/products.html', context)




def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count
    }
    
    return render(request,'accounts/customer.html', context)
            