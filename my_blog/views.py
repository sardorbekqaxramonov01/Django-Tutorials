from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req,"index.html")

def about(req):
    return render(req,"index.html")

def project(req):
    return render(req,"index.html")

def my_blog(req):
    return render(req,"index.html")

def contact(req):
    return render(req,"index.html")