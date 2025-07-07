from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(request):
    student = [
        {'id' : 1, 'name' : 'Abdullah', 'section' : 'B'}
    ]
    return HttpResponse(student)