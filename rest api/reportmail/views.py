from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Q




# Create your views here.
def index(request):
    # return HttpResponse ('hii')
    # return render(request,'reportmail.html')

    queryset = Student.objects.all()

    # if request.GET.get("search"):
    #     search_data = request.GET.get("search") 
    #     queryset = Student.objects.filter(name__icontains=search_data)

    # paginator = Paginator(queryset, 2)  # ketlo data joi chhe

    # page_number = request.GET.get("page",1)   # page nuber set krvana ketla pege pr ketla data jota che tenakki krva
    # page_obj = paginator.get_page(page_number) # http://127.0.0.1:8000/?page=1     # ?page=2   #?page=3   #?page=4 #?page=5

    return render(request,'reportmail.html',{'queryset':queryset})
    # return render(request,'reportcard.html',{'queryset':page_obj})  # queryset ni badle page_obj ly lidhu+

def marks(request,id):

    ranks =  Student.objects.annotate(marks = Sum('subjectmarks__marks')).order_by('-marks')
    i = 1
    current_rank = 0
    for rank in ranks:
       
        if rank.student_id.student_id==id:
            
            current_rank = i
            
        i = i+1

    
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = id)
    total =  queryset.aggregate(total = Sum('marks'))
    return render(request,'reportcard.html',{'queryset':queryset, 'total':total,'rank':current_rank})




from io import BytesIO
from django.core.mail import send_mail
from django.template.loader import get_template



from django.template.loader import render_to_string

from django.core.mail import EmailMessage

def sendstudentmarksemail(request,id):
        
        ranks =  Student.objects.annotate(marks = Sum('subjectmarks__marks')).order_by('-marks')
        i = 1
        current_ranks = 0
        for rank in ranks:
       
                if rank.student_id.student_id==id:
                     current_ranks = i
            
                i = i+1
        queryset = SubjectMarks.objects.filter(student__student_id__student_id = id)
        total =  queryset.aggregate(total = Sum('marks'))
        students=Student.objects.get(student_id__student_id = id)
        
                   
        html_content = render_to_string('reportcardmail.html', {'queryset': queryset, 'total': total,'rank':current_ranks})

    
        email = EmailMessage(
        subject= f'Helo, mr/miss {students.name} that is Your Progerss Report',
        body=html_content,
        from_email='avanitejani@gmail.com',
        to=[students.email],
        )
        email.content_subtype = 'html' 

        email.send()
                   
      
        return  redirect('/') 