

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import time

def index(request):
    return HttpResponse("Hello, world at" + time.strftime("%c"))