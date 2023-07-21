from django.db import models

class Contact(models.Model):
    open_time = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    branche = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    branche2 = models.CharField(max_length=255)
    location2 = models.CharField(max_length=255)
    branche3 = models.CharField(max_length=255)
    location3 = models.CharField(max_length=255)

class Footer(models.Model):
    branche = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Branches(models.Model):
    branche = models.CharField(max_length=255)
    location = models.CharField(max_length=255)