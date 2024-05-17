
# pip install faker
from faker import Faker
fake = Faker()
from .models import *
import random



# student na data add krva and koi bi rendom department add krava je aapde pele thi j stor kari raykhu hase admin side thi 
def setdata(n = 10):
    for i in range(n):
        # dept_data ni uner  Department table na data lava mare j apde stor kyra 6e te fack data nathi
        dept_data = Department.objects.all()
        # zero thi ly ne deapartment ni length  sudhi 
        r_index = random.randint(0,len(dept_data)-1)
        dept = dept_data[r_index]
        name = fake.name()
        email = fake.email()


        student_id = f"STD_{random.randint(100,999)}"
        # student_id_obj aa object return krse  #  model name nu variyable = upr no variyable 
        student_id_obj =  StudentId.objects.create(student_id = student_id)
       
    #    student no data stor krva mate 
        Student.objects.create(
            name = name,
            email = email,
            department = dept, 
            student_id =student_id_obj
        )






# pa6i badha j tudent na badhha subject na marks add krva je subject aapde admin side thi pelethi j add kari raykha 6e 
def setmarks():
    # badha student mate 
    students = Student.objects.all()
    for std in students: 
        subjects = Subject.objects.all()
        # now badha Subject ne Iterat kravsu
        for sub in subjects:  # jetli var aa Iterat thay telti var subject stor kravta javanu and marks srot kravta javana
            SubjectMarks.objects.create(
                student = std,
                subject = sub,
                marks = random.randint(0,100)
            )


# shell thi fack student add krva 

# py .\manage.py shell
# from reportcard import fackdata
# fackdata.setdata(50)
# exit()


# shell thi fack student na marks add krva 

# py .\manage.py shell
# from reportcard import fackdata
# fackdata.setmarks()
# exit()