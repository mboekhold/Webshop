from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Part

def part_list(request):
    parts = Part.objects.all()
    output = ', '.join([str(parts) for part in parts])
    return HttpResponse(output)

