from django.db import models

# Create your models here.

# python -m pip install Pillow

class Crud(models.Model):
    Name=models.CharField(max_length=50)
    Img=models.ImageField(upload_to='static/images/')

    def __str__(self) -> str:
        return self.Name
    
class Data(models.Model):
    Name=models.CharField(max_length=50)
    Img=models.ImageField(upload_to='static/images/')

    def __str__(self) -> str:
        return self.Name
    

