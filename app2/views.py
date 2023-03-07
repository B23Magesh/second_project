from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Yadav(request):
    return HttpResponse("<h1>HI YADAV</h1>")
def Yadav2(request):
    return HttpResponse('<h3>HI YADAV SON</h3>')