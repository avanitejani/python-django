from django.shortcuts import render,HttpResponse,redirect
from .models import *
import os

# Create your views here.

def home(request):
    # return HttpResponse ("hello")
    return render(request, 'home.html')

def insert(request):
    if request.method == 'POST':
        data=request.POST
        vName=data.get('htmlName')
        vSur=data.get('htmlSur')
        vImg=request.FILES.get('htmlImg')

        Crud.objects.create(Name=vName,Surname=vSur,Img=vImg)

    allData=Crud.objects.all()
    return render(request, 'insert.html',{'allData':allData})

def delete(request,id):
    data = Crud.objects.get(id=id)
    data.delete()
    return redirect('ins')

def edit(request,id):
    udata= Crud.objects.get(id=id)
    if request.method == 'POST':
        data= request.POST
        udata.Name=data.get('htmlName')
        udata.Surname=data.get('htmlSur')
        if len(request.FILES) != 0:  # jo img pele thi અપલોડ kareli hase to aalg vadhse
            if udata.Img != "": #અપલોડ કરેલ ફાઇલ ખાલી નથી nathi તો તે last img ફાઈલને સિસ્ટમમાંથી કાઢી દે છે os.remove thi
                os.remove(udata.Img.path)
                udata.Img =request.FILES.get('htmlImg')
            else:
                udata.Img =request.FILES.get('htmlImg')
        else:
            udata.Img=udata.Img #koi img અપલોડ nathi to te juna img path pr koi badlav vgar jai 6e

        udata.save()
        return redirect('ins')
    return render(request, 'Edit.html' ,{"data":udata})
