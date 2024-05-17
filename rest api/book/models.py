from django.db import models

# Create your models here.

class Author(models.Model):
    aname =models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.aname

class Publication(models.Model):
    pname = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.pname

class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication,on_delete=models.CASCADE)
    bname = models.CharField(max_length=20)
    image=models.ImageField(upload_to='my_image', default='img')

    def __str__(self) -> str:
        return self.bname