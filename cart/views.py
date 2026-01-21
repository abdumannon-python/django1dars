from pydoc import describe

from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
# Create your views here.
from .models import Users
class ListView(View):
    def get(self,request):
        user=Users.objects.all()
        return render(request,'index.html',{'user':user})

class CreateView(View):
    def get(self,request,pk):
        user=Users.objects.filter(id=pk).first()
        return render(request,'create_user.html',{'create_user':user})
    def post(self,request):
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        ID_kart = request.POST.get('ID_kart')
        tugulgan_kun = request.POST.get('tugulgan_kun')
        desc = request.POST.get('desc')

        user=Users.objects.create(
            name=name,
            lastname=lastname,
            ID_kart=ID_kart,
            tugulgan_kun=tugulgan_kun,
            desc=desc
        )
        user.save()
        return redirect('index')






























# def index(request):
#     data=Users.objects.all()
#     context={
#         'users':data,
#     }
#     return render(request,'index.html',context)
# def detail(request, User_id):
#     user = Users.objects.get(id=User_id)
#     return render(request, 'detail.html', {'user': user})
# def create_user(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         lastname=request.POST.get('lastname')
#         ID_kart=request.POST.get('ID_kart')
#         tugulgan_kun=request.POST.get('tugulgan_kun')
#         desc=request.POST.get('desc')
#
#         Users.objects.create(
#             name=name,
#             lastname=lastname,
#             ID_kart=ID_kart,
#             tugulgan_kun=tugulgan_kun,
#             desc=desc
#         )
#         return redirect('index')
#     return render(request,'create_user.html')
