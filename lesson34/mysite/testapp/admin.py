from django.contrib import admin

from .models import *

admin.site.register(Animal)
admin.site.register(Visitor)
admin.site.register(Ticket)
admin.site.register(Visit)

# Register your models here.
