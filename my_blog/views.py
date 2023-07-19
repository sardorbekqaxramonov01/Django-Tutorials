from django.shortcuts import render

from .models import Contact


def home(req):
    return render(req,"pages/home.html",)

def about(req):
    return render(req,"pages/about.html",)

def project(req):
    return render(req,"pages/project.html",)

def my_blog(req):
    return render(req,"pages/my_blog.html",)

def contact(req):
    data = Contact.objects.all
    context = {'data':data}
    return render(req,"pages/contact.html",context)