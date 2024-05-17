from django.shortcuts import render,HttpResponse

from django.conf import settings



from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from .models import *
from .serialzer import *

from django.db import models

# Create your views here.


def index(request):
    # return render(request,'index.html')
    return HttpResponse("This is Book page")


class BookAPI(APIView):
    # This line defines the BookAPI class, which is a subclass of APIView provided by Django REST Framework.

    # bookdata = Book.objects.all(): This line retrieves all the Book objects from the database using Django's ORM (Object-Relational Mapping).

    # book_ser = BookSerializer(bookdata, many=True): Here, BookSerializer is a serializer class responsible for converting complex data types, such as querysets and model instances, into native Python datatypes that can then be easily rendered into JSON, XML, or other content types. 

    # many=True indicates that there are multiple instances of Book to be serialized.


    def get(self,request):
        bookdata = Book.objects.all()
        book_ser = BookSerializer(bookdata,many=True)
        return Response({'bookdata':book_ser.data})
    
    def post(self,request):
        bookdata = BookSerializer(data=request.data)
        if not bookdata.is_valid():
                return Response({'status':'202','errors':bookdata.errors,'message':"something went wrong"})
        bookdata.save()
        return Response({"data":bookdata.data,"message":"Book inserted"})
    
    def put(self,request):
        try:
            pdata = Book.objects.get(id=request.data['id'])
            psdata =  BookSerializer(pdata,request.data,partial=True)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Book Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
              pdata = Book.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Book Delete"})
        except Exception as e:
            print(e)
            return Response({"message":"Id not found"})
        

        

    # from rest_framework import generics
    # class BookAPIGeneric1(generics.ListAPIView,generics.CreateAPIView):
    #     queryset = Book.objects.all()
    #     serializer_class=BookSerializer

    # class BookAPIGeneric(generics.DestroyAPIView,generics.UpdateAPIView):
    #     queryset = Book.objects.all()
    #     serializer_class=BookSerializer
    #     lookup_field='id'