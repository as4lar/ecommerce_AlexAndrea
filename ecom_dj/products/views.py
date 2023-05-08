from django.shortcuts import render, redirect
from django.views import View
from products.models import Product
from .forms import ProductCreate
# Create your views here.
class Products(View):
    def get(self, request):
        products=Product.objects.all()
        print(products)
        context={'products': products}
        return render(request, 'products/products.html', context)
class read1Product(View):
    def get(self, request, id):
        product=Product.objects.get(id=id)
        context={'product':product}
        return render(request, 'products/product.html', context)
    
class createProduct(View):
    def get(self, request):
        form=ProductCreate()
        context={'form':form}
        return render(request, 'user/form.html', context)
    
    def post(self, request):
        form= ProductCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print(form.errors)
            context={'form': form}
            return render(request, 'products/form.html', context)
        
class updateProduct(View):
    def get(self, request,id):
        product=Product.objects.get(id=id)
        form=ProductCreate(instance=product)
        context={'form':form}
        return render(request, 'products/form.html', context)
    
    def post(self, request,id):
        product=Product.objects.get(id=id)
        form= ProductCreate(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print(form.errors)
            context={'form': form}
            return render(request, 'products/form.html', context)
        
class deleteProduct(View):
    def get(self, request,id):
        product=Product.objects.get(id=id)
        form=ProductCreate(instance=product)
        context={'form':form}
        return render(request, 'products/formdelete.html', context)
    def post(self, request,id):
        product=Product.objects.get(id=id)
        product.delete()
        return redirect('products')

productsQueue=[]
total=0
class makeOrder(View):
    def get(self, request,id):
        product=Product.objects.get(id=id)
        context={'product': product}
        global total
        total+=int(product.price)
        productsQueue.append(product)
        print(total)
        print(productsQueue)
        return render(request, 'products/product.html', context)
        

