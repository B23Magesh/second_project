from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Muni(request):
    return HttpResponse('<h1>HI MUNI </h1>')
def Muni2(request):
    return HttpResponse("<h2>Hi Muni's Son</h2>")