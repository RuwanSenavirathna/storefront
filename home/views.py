from customer.views import register
from django.shortcuts import render
from django.http import HttpResponse
from customer.models import Customer, Register

def index(request):
    customer = Customer.objects.all()
    register = Register.objects.all()
    return render(request, 
                'storefront/index.html',
                 {'customer': customer,
                 'registers' : register 
                 }
                )
   