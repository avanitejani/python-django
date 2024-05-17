from django.db import models

# Create your models here.

class user(models.Model):
    uname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.uname