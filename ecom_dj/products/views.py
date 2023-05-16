from django.shortcuts import render, redirect
from django.views import View
from products.models import Product, Brand
from .forms import ProductCreate, BrandCreate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
# Create your views here.
productsQueue=[]
total=0
class Products(LoginRequiredMixin,View):
    def get(self, request):
        if request.user.groups.filter(name='admins').exists():
            products=Product.objects.all()
            print(products)
            context={'products': products}
            return render(request, 'products/productsAdmin.html', context)
        else:
            products=Product.objects.all()
            print(products)
            context={'products': products}
            return render(request, 'products/products.html', context)
        
class Logout(View):
    def get(self, request):
        logout(request)
        productsQueue.clear()
        total=0
        redirect('index')
    
class read1Product(View):
    def get(self, request, id):
        product=Product.objects.get(id=id)
        context={'product':product}
        return render(request, 'products/product.html', context)
    
class createProduct(View):
    def get(self, request):
        form=ProductCreate()
        context={'form':form}
        return render(request, 'products/form.html', context)
    
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
    
class deleteProdQ(View):
    def get(self, request,id):
        product=Product.objects.get(id=id)
        form=ProductCreate(instance=product)
        context={'form':form}
        return render(request, 'cart/cartprods.html', context)
    def post(self, request,id):
        product=Product.objects.get(id=id)
        global total
        total-=int(product.price)
        productsQueue.remove(product)
        return redirect('products')
    
class makeOrder(View):
    def get(self, request,id):
        product=Product.objects.get(id=id)
        print("Productoo:", product)
        global total
        total+=int(product.price)
        productsQueue.append(product)
        context={'productos': productsQueue,'total':total}
        print(total)
        print(productsQueue)
        return render(request, 'cart/cartprods.html', context)
    
class getOrders(View):
    def get(self, request):
        context={'productos': productsQueue}
        return render(request, 'cart/cartprods.html', context)
    
class payOrder(View):
    def get(self, request):
        messages.success(request,'¡Gracias por su compra!')
        productsQueue.clear()
        global total
        total=0
        return redirect('index')

"""-----------------------------------------------------------------------------------"""
class Brands(LoginRequiredMixin,View):
    def get(self, request):
            if request.user.groups.filter(name='admins').exists():
                brands=Brand.objects.all()
                print(brands)
                context={'brands': brands}
                return render(request, 'brands/brandsAdmin.html', context)
            else:
                brands=Brand.objects.all()
                print(brands)
                context={'brands': brands}
                return render(request, 'brands/brands.html', context)
            
class createBrand(View):
    def get(self, request):
        form=BrandCreate()
        context={'form':form}
        return render(request, 'brands/form.html', context)
    
    def post(self, request):
        form= ProductCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brands')
        else:
            print(form.errors)
            context={'form': form}
            return render(request, 'brand/form.html', context)

class updateBrand(View):
    def get(self, request,id):
        brand=Brand.objects.get(id=id)
        form=BrandCreate(instance=brand)
        context={'form':form}
        return render(request, 'brands/form.html', context)
    
    def post(self, request,id):
        brand=Brand.objects.get(id=id)
        form= BrandCreate(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brands')
        else:
            print(form.errors)
            context={'form': form}
            return render(request, 'brands/form.html', context)
        
class deleteBrand(View):
    def get(self, request,id):
        brand=Brand.objects.get(id=id)
        form=BrandCreate(instance=brand)
        context={'form':form}
        return render(request, 'brands/formdelete.html', context)
    def post(self, request,id):
        brand=Brand.objects.get(id=id)
        brand.delete()
        return redirect('brands')