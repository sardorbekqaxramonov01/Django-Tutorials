from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self) -> str:
        return self.name