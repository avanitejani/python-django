from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
      return self.name
    





  #  SET_NULL:  thi  foreign key mathi value aavti hoi to a delete thata prduct ni value null thay jase

  # ex..  category = models.ForeignKey(Category,on_delete=models.SET_NULL)
   
  #  CASCADE: thi  foreign key mathi value aavti hoi to a delete thata prduct ni value bi delete thy jase thay jase

  # ex..  category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Category(models.Model):
    catname = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.catname

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pname = models.CharField(max_length=20)
    price = models.IntegerField()
    qty = models.IntegerField()

    def __str__(self) -> str:
        return self.pname

   

   
    
#   model.  set_null
# model.casced