from django.shortcuts import render


def home(req):
    context = {"name" : "Sardor"}
    return render(req,"pages/home.html", context)

def about(req):
    return render(req,"pages/about.html",)

def project(req):
    return render(req,"pages/project.html",)

def my_blog(req):
    return render(req,"pages/my_blog.html",)

def contact(req):
    return render(req,"pages/contact.html",)