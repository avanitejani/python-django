from django.db import models

# Create your models here.


class Department(models.Model):
    deptname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.deptname


class Employee(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=30)
    salary=models.IntegerField()
    # salary=models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.name









# py \p
# py ./manage.py shell
# from modelapp import fackdata   (*)
# fackdata.setdata()
#  


# from modelapp.models import *
# employes.objects.all()

# limit:
# employes.objects.all()[5:7]

# oderby:
# employes.objects.all().oder_by('name')
# revers:  --  employes.objects.all().oder_by('-name')      model.objects.all().order_by('fieldname')

# revers:  --  employes.objects.all().oder_by('-name').values()

# filter:
# employes.objects.filter(name=" ").value()

# aa name sivay na data:
# employes.objects.exclude(name=" ").value()

# column:
# employes.objects.exclude(name=" ").value_list()

# employes.objects.filter(salary__gt=2000)

# employes.objects.filter(salary__gt=2000).value_list("salary")

# employes.objects.filter(name__startswith="b")).value_list("name")

# employes.objects.filter(name__icontains="av")).value_list("name")

# in:
# employes.objects.filte(Department__deptname)
# employes.objects.filte(Department__deptname="java")
# employes.objects.filte(Department__deptname="java").values()
# employes.objects.filte(Department__deptname="java").values().count()

# L=['java','python']
# employes.objects.filte(Department__deptname__in=L).values()

# employes.objects.filte(Department__deptname__in=L).values('name')
# employes.objects.filte(Department__deptname__in=L).values('name').count()
# employes.objects.filte(Department__deptname__in=L).revers()

# exist: tue False
# employes.objects.filter(name="avani ").exist()



# from django.db.models import Avg  (*)

# - -   employes.objects.aggregate(Avg('sayary'))


# employes.objects.annotate(Max('sayary'))

# employes.objects..annotate(count(Department__deptname),(Max('sayary'))).




# pip install djangorestfremwork

