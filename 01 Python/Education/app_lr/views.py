from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
import requests   # pip install requests




# Create your views here.


def index(request):
    # response = requests.get('http://localhost:8000/app_student/')
    return render(request,'index.html')
    # return HttpResponse("This is login page")


# def send_request_to_app2(request):
#     # Make a request to App 2
#     # Example: sending a GET request
#     # Replace 'http://localhost:8000/app2/' with the actual URL of App 2's index page
#     response = requests.get('http://localhost:8000/app_student/index.html')
#     return HttpResponse('Request sent to App 2')
#     # return redirect ('app_student:index.html')