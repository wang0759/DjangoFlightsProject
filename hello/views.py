from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def second(request):
    return HttpResponse("Second page, why do we need all?")