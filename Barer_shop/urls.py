from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("", views.base, name="base"),
    path("home/", views.home, name="home"),
    path("our_story/", views.our_story, name="our_story"),
    path("service/", views.service, name="service"),
    path("price_list/", views.price_list, name="price_list"),
    path("contact/", ContactView.as_view(), name="contact"),
]