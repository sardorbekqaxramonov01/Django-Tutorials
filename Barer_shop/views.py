from django.shortcuts import render
from .models import Contact

def base(req):
    return render(req,"base.html")

def home(req):
    return render(req,"pages/home.html")

def our_story(req):
    return render(req,"pages/our_story.html")

def service(req):
    return render(req,"pages/service.html")

def price_list(req):
    return render(req,"pages/price_list.html")

def contact(req):
    data = Contact.objects.all
    context = {"data":data}
    return render(req,"pages/contact.html",context)

def base(req):
    data = Contact.objects.all
    context = {"data":data}
    return render(req,"pages/base.html.html",context)