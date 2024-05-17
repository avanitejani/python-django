from django.db import models
# python -m pip install Pillow

# Create your models here.
class Crud(models.Model):
    Name=models.CharField(max_length=25)
    Like=models.CharField(max_length=100)
    Gender=models.CharField(max_length=25)
    Img=models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.Name
    