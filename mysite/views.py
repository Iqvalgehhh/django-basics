# 5
from django.http import HttpResponse
from django.shortcuts import render

# 6
def home(request):
    return render(request, 'home.html')