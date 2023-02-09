from django.shortcuts import render
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    return render(request,"ecomapp/index.html")


def collections(request):

    category = Category.objects.filter(status=0)
    context = {'category':category}

    return render(request,"ecomapp/collections.html", context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products = Product.objects.filter(category__slug = slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category':category}
        return render(request,"ecomapp/products/index.html", context)
    
    else: 
        messages.warning(request, "No such Category Found")
        return redirect('collections')
        


def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products = Product.objects.filter(slug=prod_slug,status=0).first()
            context = {'products':products}

        
        else:
            messages.error(request, "No Such Product not found")
            return redirect('collections')
        return render(request,"ecomapp/products/view.html", context)
        

        
           
    else:
        messages.error(request, "No Such category not found")
        return redirect('collections')
      
    





