from django.shortcuts import render


def home(req):
    return render(req,"base.html",)

def about(req):
    return render(req,"pages/about.html",)

def appointment(req):
    return render(req,"pages/appointment.html",)

def blog(req):
    return render(req,"pages/blog.html",)

def blog_singel(req):
    return render(req,"pages/blog-singel.html",)

def contact(req):
    return render(req,"pages/contact.html",)

def department(req):
    return render(req,"pages/department.html",)

def doctor(req):
    return render(req,"pages/doctor.html",)

def pricing(req):
    return render(req,"pages/pricing.html",)

