from django.shortcuts import render
from .models import Employee
# Create your views here.

def home(request):
    employee = Employee.objects
    return render(request, 'main.html', {'employee': employee})

def training(request):
    return render(request,'training.html')

def team(request):
    employee = Employee.objects
    return render(request, 'team.html', {'employee': employee})

def about(request):
    return render(request, 'about.html')