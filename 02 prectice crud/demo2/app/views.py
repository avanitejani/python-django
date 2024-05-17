from django.shortcuts import render,redirect
# from django.shortcuts import HttpResponse
from .models import *
import os

# Create your views here.

def index(request):
    # return  HttpResponse ('hii ')
    return render(request, 'index.html')

def reg(request):
    if request.method == 'POST':
        data=request.POST
        vname=data.get('hname')
        vimg=request.FILES.get('himg')

        Crud.objects.create(Name=vname,Img=vimg)                
   
    allData=Crud.objects.all()
    return render(request, 'reg.html',{'allData':allData})

#         Crud.objects.create(Name=vname,Img=vimg)
#     else:
#         allData=Crud.objects.all()
#         return render(request, 'reg.html',{'allData':allData})
#     return render(request, 'reg.html')

   

def delete(request,id):
    data = Crud.objects.get(id=id)
    data.delete()
    return redirect('reg')

def edit(request,id):
    udata = Crud.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        udata.Name=data.get("hname")
        # udata.Img=data.get("img")
        if len(request.FILES) != 0:
            if udata.Img != "":
                os.remove(udata.Img.path)
                udata.Img= request.FILES.get('himg')
            else:
                udata.Img= request.FILES.get('himg')
        else:
            udata.Img=udata.Img
    
        udata.save()
        return redirect('reg')
    
    return render(request,'update.html',{"data":udata})



