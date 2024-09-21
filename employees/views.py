from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from employees.models import Employee

#a12
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    #a15
    context ={
        'employee': employee,
    }
    #a13
    return render(request, 'employee_detail.html', context)