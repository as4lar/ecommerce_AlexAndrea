from django.shortcuts import render, redirect
from django.views import View
from user.models import User
from .forms import UserCreate
# Create your views here.
class Users(View):
    def get(self,request):
        users=User.objects.all()
        context={'users': users}
        return render(request, 'user/user.html', context)
    
class createUser(View):
    def get(self, request):
        form=UserCreate()
        context={'form':form}
        return render(request, 'user/form.html', context)
    
    def post(self, request):
        form= UserCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
        else:
            print(form.errors)
            context={'form': form}
            return render(request, 'user/form.html', context)
        
class updateUser(View):
    def get(self, request,id):
        user=User.objects.get(id=id)
        form=UserCreate(instance=user)
        context={'form':form}
        return render(request, 'user/form.html', context)
    
    def post(self, request,id):
        user=User.objects.get(id=id)
        form= UserCreate(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')
        else:
            print(form.errors)
            context={'form': form}
            return render(request, 'user/form.html', context)
        
class deleteUser(View):
    def get(self, request,id):
        user=User.objects.get(id=id)
        form=UserCreate(instance=user)
        context={'form':form}
        return render(request, 'user/formdelete.html', context)
    def post(self, request,id):
        user=User.objects.get(id=id)
        user.delete()
        return redirect('user')
