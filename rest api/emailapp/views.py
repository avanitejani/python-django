from django.shortcuts import render,HttpResponse
from .utils import *

# Create your views here.



# m nm mail moklva mate 

def sendmail(request):
    # send_mail_to_client()
    # return render(request,'index.html')
    return HttpResponse("This Mail sent...")




# file attetch kari ne mail molva mate 

def sendmail(request):
    filepath = f"{settings.BASE_DIR}/template/index.html"  # setting path aavse  BASE_DIR aa. aani under index.html 
    mail_with_file(filepath)
    return HttpResponse("This file Mail sent...")
