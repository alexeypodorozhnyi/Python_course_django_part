from django.contrib import admin

# Register your models here.
from .models import Item, Profile, ShoppingEvent, ReversalEvent

admin.site.register(Item)
admin.site.register(Profile)
admin.site.register(ShoppingEvent)
admin.site.register(ReversalEvent)
