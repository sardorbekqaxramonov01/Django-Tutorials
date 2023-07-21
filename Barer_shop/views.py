from django.shortcuts import render
from .models import *

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
    date = Footer.objects.all
    datta = Branches.objects.all
    context = {"data":data,"data":date,"data":datta }
    return render(req,"base.html",context)