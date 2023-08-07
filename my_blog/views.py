from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def home(req):
    return render(req,"pages/home.html",)

def about(req):
    return render(req,"pages/about.html",)

def project(req):
    return render(req,"pages/project.html",)

class BlogPageView(ListView):
    model = Blog
    template_name = "pages/blog.html"
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["Blog"] = Blog.objects.all()
        return context
    
class BlogSingleView(DetailView):
    model = Blog
    template_name = "pages/blog_single.html"
    

def contact(req):
    data = Contact.objects.all
    context = {'data':data}
    return render(req,"pages/contact.html",context)