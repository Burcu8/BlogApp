from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def index(request): 
    return HttpResponse("Home Page")

def blogs(request): 
    return HttpResponse("Blogs")

def blog_details(request,id): 
    return HttpResponse("Blog details" + id) 