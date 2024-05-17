from django.shortcuts import render,HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Q



# Create your views here.

def index(request):
    queryset = Student.objects.all()

    if request.GET.get("search"):
        search_data = request.GET.get("search") 
        queryset = Student.objects.filter(name__icontains=search_data)

    paginator = Paginator(queryset, 2)  # ketlo data joi chhe

    page_number = request.GET.get("page",1)   # page nuber set krvana ketla pege pr ketla data jota che tenakki krva
    page_obj = paginator.get_page(page_number) # http://127.0.0.1:8000/?page=1     # ?page=2   #?page=3   #?page=4 #?page=5

    # return render(request,'reportcard.html',{'queryset':queryset})
    return render(request,'reportcard.html',{'queryset':page_obj})  # queryset ni badle page_obj ly lidhu

# def search(request):
#     if request.method=="GET":
#          query = request.GET['ser']
#          all_product=Student.objects.filter(Q(name__icontains=query)|Q(name__icontains=query))
#          return render(request,'reportcard.html',{"all_product":all_product})
#     else:
#          return render(request,'reportcard.html')



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
    return render(request,'card.html',{'queryset':queryset, 'total':total,'rank':current_rank})


