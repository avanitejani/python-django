from django.shortcuts import render,redirect
from .models import User
import os


# Create your views here.

def index (request):
    return render(request, 'index.html')

def InsertData (request):
    if request.method =='POST':
        # data=request.POST
        # name=data.get('name')
        # email=data.get('email')
        # img = request.FILES.get('img')

        viwesname=request.POST['htmlname']
        viwesemail=request.POST['htmlemail']
        viewsimg= request.FILES["htmlimg"] 
    
        newuser = User.objects.create(
            name=viwesname,
            email=viwesemail,
            img=viewsimg,
        )
        return redirect('show')

    # return render(request, 'show.html')

        # return redirect('showpage')
    
#    data fatching  
def showpage(request):
    alldata = User.objects.all()
    return render(request, 'show.html',{'key1':alldata})

def editpage(request,pk):
    onedata = User.objects.get(id=pk)
    return render(render,'edit.html',{'key2':onedata} )


def updatData(request,pk):
    viwes = User.objects.get
    viwes.name=request.POST['htmlname']
    viwes.email=request.POST['htmlemail']
    # views.img= request.FILES["htmlimg"] 

    # if len(request.FILES) !=0 :
    #     if viwes.img != "":
    #         os.remove(viwes.img.path)
    #         viwes.img = request.FILES.get('img')
    #     else:
    #         viwes.img = request.FILES.get('img')
    # else:
    #     viwes.img=viwes.img  

    viwes.save() 
    return redirect('show')

# def deleteData(request,pk):
#     ddata= User.objects.get(id=pk) 
#     ddata.delete()
#     return redirect('show')