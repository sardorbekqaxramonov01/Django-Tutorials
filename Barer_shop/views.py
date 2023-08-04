from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView

def home(req):
    branche = Branche.objects.all()
    context = {
        "branche":branche
        }
    return render(req,"pages/home.html",context)

def our_story(req):
    branche = Branche.objects.all()
    barber = Barbers.objects.all()
    context = {
        "branche":branche,
        "barber":barber
        }
    return render(req,"pages/our_story.html",context)

def service(req):
    branche = Branche.objects.all()
    service = Service.objects.all()
    context = {
        "branche":branche,
        "service":service,
        }
    return render(req,"pages/service.html",context)

def price_list(req):
    branche = Branche.objects.all()
    price = Price.objects.all()
    context = {
            "price":price,
            "branche":branche
        }
    return render(req,"pages/price_list.html",context)

# def contact(req):
#     contact = Contact.objects.all()
#     branche = Branche.objects.all()
#     context = {
#         "contact":contact,
#         "branche":branche,
#         }
#     return render(req,"pages/contact.html",context)

def base(req):
    branche = Branche.objects.all()
    context = {
        "branche":branche
        }
    return render(req,"base.html",context)


class ContactView(TemplateView):
    template_name = 'pages/contact.html'