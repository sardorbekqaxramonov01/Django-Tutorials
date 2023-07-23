from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("doctor/", views.doctor, name="doctor"),
    path("department/", views.department, name="department"),
    path("pricing/", views.pricing, name="pricing"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
]