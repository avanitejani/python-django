from django.shortcuts import render,HttpResponse
import requests
import random


# Create your views here.

def sendsms(request):
    url = "https://www.fast2sms.com/dev/bulkV2"

    otp = random.randint(100000,999999)
    # otp mate 
    # querystring = {"authorization":"WXfAe5cjnlMG0thTkdLD9IsgRyZbS7w41UzP3H8mKiqQNVEova9vDJtywEXpMNoUieOfPlq1r8HhdnTL","":"Hello, this is api testing","variables_values":otp,"route":"otp","numbers":"9265586214"}

    # msg mate 
    # querystring = {"authorization":"WXfAe5cjnlMG0thTkdLD9IsgRyZbS7w41UzP3H8mKiqQNVEova9vDJtywEXpMNoUieOfPlq1r8HhdnTL","message":"This is test message","language":"english","route":"q","numbers":"9265586214"}


    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return HttpResponse("sms sent...")