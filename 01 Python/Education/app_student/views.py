from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
# Create your views here.


# def index(request):
#     return render(request,'sindex.html')
#     # return HttpResponse("This is Student page")


# def app1(request):
#     # Handle the request from App 1
#     # Example: returning a response
#     return HttpResponse('Request received from App 1')
def index(request):
    return render(request, 'index.html')