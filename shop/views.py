from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'shop/index.html')

def register(request):
    return render(request,'shop/register.html')

def collections(request):
    cat=Category.objects.filter(status=0)
    return render(request,'shop/collections.html',{"category":cat})


def collectionsView(request,name):
    if(Category.objects.filter(name=name,status=0)):
        product=Product.objects.filter(category__name=name)
        return render(request,"shop/product/views.html",{"product":product,"cat":name})
    else:
        messages.warning(request,"No Such Category Found")
        return render(request,"shop/collections.html")