from django.contrib import admin
from .models import BakeryInfo, Items, ContactInfo

# Register your models here.
admin.site.register(BakeryInfo)
admin.site.register(Items)
admin.site.register(ContactInfo)
