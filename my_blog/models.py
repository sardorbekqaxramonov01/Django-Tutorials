from django.db import models

class Contact(models.Model):
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

