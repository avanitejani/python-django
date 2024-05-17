from django.db import models

# python -m pip install Pillow

# Create your models here.

class User(models.Model):
    name =models.CharField(max_length=50)
    email =models.CharField(max_length=50)
    img=models.ImageField(upload_to='public/static/images/')

    def __str__(self) -> str:
            return self.name
    
  