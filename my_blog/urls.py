from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("project/", views.project, name="project"),
    path("contact/", views.contact, name="contact"),
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("blog/<int:pk>/", BlogSingleView.as_view(), name="blog_single"),
]