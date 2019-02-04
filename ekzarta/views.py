from django.shortcuts import render
from .models import Employee,Reviews


def home(request):
    review = Reviews.objects
    return render(request, 'main.html', {'review': review})

def training(request):
    review = Reviews.objects
    return render(request,'training.html', {'review': review})

def team(request):
    review = Reviews.objects
    employee = Employee.objects
    return render(request, 'team.html', {'employee': employee, 'review': review})

def about(request):
    review = Reviews.objects
    return render(request, 'about.html', {'review': review})
