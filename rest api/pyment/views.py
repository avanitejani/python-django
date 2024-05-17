
# Create your views here.

# pip install django-cors-headers
# pip install razorpay
# pip install --upgrade setuptools 

from django.shortcuts import render
from django.http import JsonResponse
import razorpay
from .models import *



client = razorpay.Client(auth=('rzp_test_eyW5z7ycuJ3MDH','8YgEuwlC7VDuL6RrbzpYRkDu'))
# Create your views here.


def pay(request,amt):
    amount = int(amt)*100 
    print(amount)
    # aa oder generate thase request call kriye tyare  
    data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
    p = client.order.create(data=data)  
    
    # return render(request,'pay.html',{'data':p})
    return JsonResponse(p)


def payment(request):
    return render(request,'pay.html')

# pycache 
# model import krvi pa6i aena funvction ne aevu use kariye varaghadi ae te data 1k cache ma rey tene pycache kevay 

#  PyPI
    #  peip
# python ma new update aayvu j teni information aape
