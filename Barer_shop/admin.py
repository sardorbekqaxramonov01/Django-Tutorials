from django.contrib import admin


from .models import *
admin.site.register(Barbers)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Branche)
admin.site.register(Price)