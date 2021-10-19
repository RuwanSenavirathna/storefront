from django.shortcuts import render
from django.http import HttpResponse
from . models import Customer, Register

def index(request):
    customer = Customer.objects.all()
    return render(request, 'index.html', {'customer': customer })

def register(request):
    register = Register.objects.all()
    return render(request, 'register.html', {'registers': register })

def information(request):
    return HttpResponse('This is INFO page')