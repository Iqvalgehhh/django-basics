# 5
from django.http import HttpResponse
from django.shortcuts import render
#a8
from employees.models import Employee

# 6
def home(request):
    #a7
    employees = Employee.objects.all()
    context = {
        'employees' : employees,
    }
    return render(request, 'home.html', context)