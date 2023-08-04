from django.db import models


class Barber(models.Model):
     Image = models.ImageField(upload_to="media")
     name = models.CharField(max_length=255)

class Service(models.Model):
     Image = models.ImageField(upload_to="media")
     Services = models.CharField(max_length=255)
     Price = models.FloatField(max_length=6)

class Price(models.Model):
     photo = models.ImageField(upload_to="media")
     starting = models.FloatField(max_length=6)
     Haircut = models.FloatField(max_length=6)
     Beard_Trim = models.FloatField(max_length=6)
     Razor_Cut = models.FloatField(max_length=6)
     Shaves = models.FloatField(max_length=6)
     Styling_Color = models.FloatField(max_length=6)

class Contact(models.Model):
    open_time = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Branche(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

