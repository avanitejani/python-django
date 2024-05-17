from django.shortcuts import render,HttpResponse
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .serialzer import *

from rest_framework.views import APIView


# Create your views here.

class DataAPI(APIView):

    def get(self, request):
        allData = Data.objects.all()
        seralizer = DataSerealizer(allData,many=True)
        return Response({'apidata':seralizer.data})
        
    def post(self, request):
        data = DataSerealizer(data=request.data)
        if not data.is_valid():
            return Response({'message':"something went wrong"})
        data.save()
        return Response({'apidata':data.data,'message':"data inserted"})
    
    def put(self,request):
        try:
            sdata=Data.objects.get(id=request.data['id'])
            sdata = DataSerealizer(data=request.data)
            if not sdata.is_valid():
                return Response({'message':"something went wrong"})
            sdata.save()
            return Response({"data":sdata.data,"message":"Student Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})

    def delete(self,request):
        try:
            sdata=Data.objects.get(id=request.data['id'])
            sdata.delete()
            return Response({"message":"Student Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})