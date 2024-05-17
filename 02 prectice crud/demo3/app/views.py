from django.shortcuts import render,HttpResponse,redirect
from .models import *
import os


# Create your views here.

def index(request):
    # return HttpResponse ('hello')
    return render (request,'index.html')

def insert(request):
    if request.method == 'POST':
        data = request.POST
        vName = data.get('htmlName')
        vLike=data.getlist('htmlLike')
        vGenders=data.get('htmlGender')
        vImg=request.FILES.get('htmlImg')

        likeit=''
        for i in vLike:
            likeit=likeit+i+','  # print(likeit)
        
        Crud.objects.create(Name=vName,Like=vLike,Gender=vGenders,Img=vImg)

    allData=Crud.objects.all()
    return render (request,'insert.html',{'allData':allData})

    
def delete(request,id):
    data= Crud.objects.get(id=id)
    data.delete()
    return redirect ('add')

def edit(request,id):
    udata=Crud.objects.get(id=id)

    if request.method == 'POST':
        data=request.POST
        udata.Name=data.get('htmlName')
        Like=data.getlist('htmlLike')
        udata.Gender=data.get('htmlGender')

        # checbox list
        likeit=''
        for i in Like:
            likeit=likeit+i+','  # 
            
        print(likeit)
        udata.Like=likeit


        # img 
        if len(request.FILES) !=0:
            if udata.Img != '':
                os.remove(udata.Img.path)
                udata.Img = request.FILES.get('htmlImg')
            else:
                udata.Img = request.FILES.get('htmlImg')
        else:
            udata.Img=udata.Img



        udata.save()
        return redirect ('add')
    

    return render(request,'edit.html',{"data":udata})