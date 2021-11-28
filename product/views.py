from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
# Create your views here.

def home(request):
    return render(request, 'product/index.html')


def post(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        weight = request.POST['weight']
        price = request.POST['price']

        product  = Product.objects.create(product_name=product_name,weight=weight,price=price)
        product.save()
    
    return redirect('/')