# pip install djangorestframework
#  python.exe -m pip install --upgrade pip

from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

# database models import krva 
# from .models import Student
from .models import *

# serializer import krva mate 
# from .serialzer import StudentSerealizer
from .serialzer import *

from rest_framework.views import APIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Simple JWT can be installed with pip:
# pip install djangorestframework-simplejwt

from rest_framework_simplejwt.views import TokenVerifyView

# JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


# 2024-04-03 api with tokan 

  # tokan authontication  aetle user register kare to j data dekhay 

#    'rest_framework.authtoken': project ni setting ma aap add kyra and rest_framework add kyra pa6i 'rest_framework.authtoken' add krvu



class RregisterUser(APIView):
     def post(self,request):
        user = UserSeralizer(data=request.data)
        if not user.is_valid():
                return Response({'status':'202','errors':user.errors,'message':"something went wrong"})
        user.save()
        udata = User.objects.get(username=request.data['username'])
        refresh = RefreshToken.for_user(udata)
        
        return Response({"data":user.data,'refresh': str(refresh),
        'access': str(refresh.access_token),"message":"Student inserted"})


#   two model dta table method                          

class StudentAPI(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        studentdata = Student.objects.all()
        seralizer = StudentSerealizer(studentdata,many=True)
        return Response({'apidata':seralizer.data})

    def post(self,request):
            sdata =  StudentSerealizer(data=request.data)
            if not sdata.is_valid():
                return Response({'status':'202','errors':sdata.errors,'message':"something went wrong"})
            sdata.save()
            return Response({"data":sdata.data,"message":"Student inserted"})
    

    def put(self,request):
        try:
            sdata = Student.objects.get(id=request.data['id'])
            sdata =  StudentSerealizer(sdata,request.data)
 
            if not sdata.is_valid():
                return Response({'status':'202','errors':sdata.errors,'message':"something went wrong"})  
            
            sdata.save()
            return Response({"data":sdata.data,"message":"Student Updated"})
        
        except Exception as e:
            return Response({"message":"Id not found"})
        

    def delete(self,request):
        try:
              sdata = Student.objects.get(id=request.data['id'])
              sdata.delete()
              return Response({"message":"Student Delete"})
        
        except Exception as e:
              return Response({"message":"Id not found"})
        


class ProductAPI(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        print(request.user)
        prodata = Product.objects.all()
        seralizer = ProductSerializer(prodata,many=True)
        return Response({'apidata':seralizer.data})
    


#    post in body: {
#     "pname": "perfum",
#     "price": 522,
#     "qty": 20,
#     "category": 1
# }
    

    def post(self,request):
            prodata =  ProductSerializer(data=request.data)
            if not prodata.is_valid():
                return Response({'status':'202','errors':prodata.errors,'message':"something went wrong"})
            prodata.save()
            return Response({"data":prodata.data,"message":"Product inserted"})
    


#    put in body: {
#   "id":6,
#     "pname": "perfum-u",
#     "price": 550,
#     "qty": 50,
#     "category": 3
# }
    

    def put(self,request):
        try:
            pdata = Product.objects.get(id=request.data['id'])
            psdata =  ProductSerializer(pdata,request.data)

            if not psdata.is_valid():
                return Response({'status':'202','errors':psdata.errors,'message':"something went wrong"})  
            
            psdata.save()
            return Response({"data":psdata.data,"message":"Product Updated"})
        except Exception as e:
            return Response({"message":"Id not found"})
        

#   put in body: 
# { 
#      "id":4
#  }

    def delete(self,request):
        try:
              pdata = Product.objects.get(id=request.data['id'])
              pdata.delete()
              return Response({"message":"Product Delete"})
        except Exception as e:
            return Response({"message":"Id not found"})















# 2024-04-01 normal api crud



  # @api_view(['GET'])
  # def index(request):
  #     return Response({'message':'Get API calling'})


  # data get krva mate 
@api_view(['GET'])
def index(request):
    studentdata = Student.objects.all()
    serialzer = StudentSerealizer(studentdata , many=True)
    return Response({'apidata':serialzer.data,'message':'Get API calling'})

@api_view(['POST']) 
def add_student(request):
    data = request.data
    addData = StudentSerealizer(data=request.data)

    if not addData.is_valid():
        return Response({'status':'202','errors':addData.errors,'message':"something went wrong"})
    
    addData.save()
    return Response({"data":addData.data,"message":"Student inserted"})

    # put thi update krci to data ni badhi valu type karine change krvi pade koi 1k pertiqular fild change ny thay

    # and 

    # patch thi update krvi to aapde je 1k file change krvi hoi to thse 

@api_view(['PUT'])
def update_student(request,id):
    sdata = Student.objects.get(id=id)
    sdata =  StudentSerealizer(sdata,request.data)

    if not sdata.is_valid():
        return Response({'status':'202','errors':sdata.errors,'message':"something went wrong"})  
    
    sdata.save()
    return Response({"data":sdata.data,"message":"Student Updated"})




@api_view(['DELETE'])
def delete_student(request,id):
      sdata = Student.objects.get(id=id)
      sdata.delete()
      return Response({"message":"Student Deleted Successfully"})








    






# Thunder Client:  vscode extansion
# postman: goggles dd 
# django rest api documentation 