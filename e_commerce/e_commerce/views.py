from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from products.models import Products



def index(request):
    name= "John Doe"
    description="A sample description"
    price= 29.99
    stock= 10
    
    # bulk create
    p=Products.objects.create(name=name,description=description,price=price,stock=stock)
    
    data={'message':'Hello, welcome to the e-commerce site!'}
    return render(request,'index.html',context=data)


def index1(request):
    products = Products.objects.all()
    data = {'products': products}
    return render(request, 'index.html', context=data)