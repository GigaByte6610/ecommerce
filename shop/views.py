from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from math import ceil
# Create your views here.
def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlides=n//4 + ceil((n/4)-(n//4))
    # params={ 'no of slides':nSlides,'range':range(1,nSlides),'product':products}
    allProds=[[products,range(1,nSlides),nSlides],
             [products,range(1,nSlides),nSlides]]
    params={'allProds':allProds}
    return  render(request,'shop/index.html',params)

def about(request):
    return  render(request,'shop/about.html')

def contact(request):
    return  render(request,'shop/index.html')

def tracker(request):
    return  render(request,'shop/index.html')

def search(request):
    return  render(request,'shop/index.html')

def prodView(request):
    return  render(request,'shop/index.html')

def checkout(request):
    return  render(request,'shop/index.html')

