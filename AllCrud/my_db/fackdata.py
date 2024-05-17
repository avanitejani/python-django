# pip install faker

from faker import Faker
import random

fake = Faker()
from .models import Department,Employee 



def setdata(n=15):


    emp =  Employee.objects.all()
    for i in range(0,len(emp)-1):
        emp[i].salary = random.randint(1000,100000)
        emp[i].save()
        
    for i in range(0,n):

        departments = Department.objects.all()
        deptr =  random.randint(0,len(departments)-1)
        name =  fake.name()
        email = fake.email()
        phone = fake.phone_number()
        print(name)


        Employee.objects.create(name=name,email=email,phone=phone,department=departments[deptr])

