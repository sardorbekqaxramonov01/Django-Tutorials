from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("project/", views.project, name="project"),
    path("contact/", views.contact, name="contact"),
    path("my_blog/", views.my_blog, name="my_blog"),
]