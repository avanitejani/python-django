from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def InsertPageView(request):
    return render(request, 'insert.html')


def InsertData(request):
    # data come from HTML to view 
    # html na data viwes.py na page pr lava mate     
    #  ---> html page thi user j data submit krse te aa fnameV ma stor thase and pa6i te Student.objects.create thi Firstname nane na model database ma stor thase

    fnameV=request.POST['fname']   # ['fname'] aetle html ma inpur ma je namae aplu te
    lnameV=request.POST['lname']
    emailV=request.POST['email']
    contactV=request.POST['contact']

    # creating object of Model class  --->   from .models import *
    # inserting data into table
    newuser = Student.objects.create(
        #  Firstname=Model nu (Tabel nu)  Firstname   ||   fname=upr request.post pa6inu fname ,
        Firstname=fnameV, 
        Lastname=lnameV ,
        Email=emailV,
        Contact=contactV)
    


    # Afret Insert render on show.html
    # return render(request,'show.htm l')

    # Afret Insert render on showpage view --> aewtle data insert thatas def ShowPage call thy jase redirect thi 

    return redirect('showpage')


# show page view 

def ShowPage(request):
    # select * from tablename(Student)

    # for fatching all the data of the table 

    # kem all method kemke table ni under jetla pn data 6e te badha j show.html na page pr despley krva mate

    # {'key1':all_data} : data jyare aapde show.html ma lay ne javi tyare aene dictionry ni under lay ne javu pade

    # tayre { } 1k dictionry pass krvi pade aam django ma tene Context kevay

    all_data = Student.objects.all()
    return render(request,'show.html',{'key1':all_data})


# Edit page view 
# pk : stand for (mtlb ke) primary key 
def EditPage(request,pk):
    # Fetching the data of particular ID 
    get_data = Student.objects.get(id=pk)
    return render(request,'edit.html',{'key2':get_data})



# upsdata data view 
def UpdataData(request,pk):
    udata = Student.objects.get(id=pk)

    #  Firstname=Model nu (Tabel nu)  Firstname   ||   fname= edit.html ma form ni fild in der je name aapelu 6 tyathi aavse,
    udata.Firstname = request.POST['fname']
    udata.Lastname=request.POST['lname'] 
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']

    # quary for update 
    udata.save()

    # render to show Page 
    return redirect('showpage')

# delete data viwe 
def DeleteData(request,pk):
    ddata= Student.objects.get(id=pk)
    # Query foe delete 
    ddata.delete()
    return redirect('showpage')


     