from django.db import models

# Create your models here.


class Crud (models.Model):
    Name=models.CharField(max_length=50)
    Surname=models.CharField(max_length=50)
    Img=models.ImageField(upload_to="static/images/")

    def __str__(self):
        return self.Name
    