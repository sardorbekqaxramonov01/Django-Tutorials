from django.shortcuts import render
from .models import *

# Create your views here.
def index(req):
    post = Post.objects.all()
    context = {'post': post}
    return render(req, 'index.html', context=context)