from django.contrib import admin


from .models import *
admin.site.register(Barber)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Branche)
admin.site.register(Price)