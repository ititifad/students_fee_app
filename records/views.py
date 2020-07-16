from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.db.models import Q, Count
from .forms import RecordsForm

def is_valid_queryparam(param):
        return param != '' and param is not None

def home(request):
    qs = Records.objects.all().order_by('-publish_date')
    classrooms = Classroom.objects.all()
    students = Student.objects.all()
    students_contains_query = request.GET.get('students_contains')
    id_exact_query = request.GET.get('id_exact')
    students_or_classrooms_query = request.GET.get('students_or_classrooms')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    classroom = request.GET.get('classroom')
    student = request.GET.get('student')
    completed = request.GET.get('completed')
    not_completed = request.GET.get('notCompleted')
    
    total_students = students.count()
    completed_school_fees = qs.filter(completed='True').count()
    not_completed_school_fees = qs.filter(completed='False').count()
    
    if is_valid_queryparam(students_contains_query):
        qs = qs.filter(student__icontains=students_contains_query)
        
    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(students_or_classrooms_query):
        qs = qs.filter(Q(students__icontains=students_or_classrooms_query)
                       |Q(classrooms__name__icontains=students_or_classrooms_query)
                       ).distinct()
    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)
    
    if is_valid_queryparam(classroom) and classroom != 'Choose...':
        qs = qs.filter(classrooms__name=classroom)

    if is_valid_queryparam(student) and student != 'Choose...':
        qs = qs.filter(students__name=student)
        
    if completed == 'on':
        qs = qs.filter(completed=True)

    elif not_completed == 'on':
        qs = qs.filter(completed=False)
        
    context = {
        'queryset' : qs,
        'classrooms' : classrooms,
        'students' : students,
        'total_students' : total_students,
        'completed_school_fees' : completed_school_fees,
        'not_completed_school_fees' : not_completed_school_fees
        
    }
    return render(request, 'records/home.html', context)

def CreateRecord(request):
        if request.method == 'POST':
                form = RecordsForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        return redirect('/')
        else:
                form = RecordsForm()
                
        context = {
                'form': form
        }
        return render(request, 'records/records_form.html', context)
    