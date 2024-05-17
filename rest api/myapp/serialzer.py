from rest_framework import serializers
from .models import *

# User  import kryu 
from django.contrib.auth.models import User

class StudentSerealizer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields="__all__"

    # khali name aand email show thay
        # fields=['name','email']

    # khali age show thai
        # fields=['age']

    # age sivay na badha show thai 
        # exclude = ['age']

    def validate(self, data):

        if data['age']<18:
           raise serializers.ValidationError("Age must be more than 18")
        
        return data

        





class CategorySerealizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=['catname']
        
    

class ProductSerializer(serializers.ModelSerializer):
    # category= CategorySerealizer()   

     # Category no data lava, category na CategorySerealizer ma set karela j data aavse like: fields=['catname'] badha ny aave 
     #  but aa line lkhvathi error aave 6e  te thin def to_representation thi lavsu have 

    class Meta:
        model = Product
        fields="__all__"
        # depth=1  # category na all data aavi jase aana thi    
      

# Category no data lavva aa kam krvi chhiye 
    def to_representation(self, instance):
       self.fields['category'] =  CategorySerealizer(read_only=True)
       return super(ProductSerializer, self).to_representation(instance)
    

    # authontication(token) ma user na data j aave username and password  te aya stord karavana chhe .  

class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model=User  # User upr import kravu padse  
        fields=['username','password']


    # user name and password stor kare  create method no use kari user ma data j aavse te stor karse
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user