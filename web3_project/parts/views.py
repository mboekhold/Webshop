from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Part

def part_list(request):
    parts = Part.objects.all()
    return render(request,'parts/part_list.html', {'parts': parts})

