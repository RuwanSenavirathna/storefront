from django.shortcuts import render
from django.http import HttpResponse

para_data = {
    'name' : 'Ruwan',
    'age' : 34,
    'place' :'Kadawatha'
}
def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    x = calculate()
    y = 2
    return render(request, 'hello.html', {'name' : 'Ruwan'})


def new(request):
    return render(request, 'new.html', para_data)
    # return HttpResponse("This is new OK")