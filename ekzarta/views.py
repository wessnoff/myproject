from django.shortcuts import render
from .models import Employee
# Create your views here.

def home(request):
    employee = Employee.objects
    return render(request, 'home.html', {'employee': employee})
