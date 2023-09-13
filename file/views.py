from django.shortcuts import render
from .models import *

# Create your views here.
def index(req):
    car = Car.objects.all()
    context = {'car': car}
    return render(req, 'index.html', context)