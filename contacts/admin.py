from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models.contact_model import Contact
from .models.phoneNumber_model import PhoneNumber

admin.site.register(Contact)
admin.site.register(PhoneNumber)
