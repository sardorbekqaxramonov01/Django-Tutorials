from django.shortcuts import render

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
    return render(req,"pages/contact.html")