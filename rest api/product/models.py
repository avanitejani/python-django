from django.db import models

# Create your models here.


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=10)
    

    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=10)
    # Add other fields as needed

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    pro_name = models.CharField(max_length=10)
    pro_price=models.IntegerField()
    pro_qty=models.IntegerField()
    pro_desc=models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self) -> str:
        return self.pro_name
