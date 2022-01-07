from django.contrib import admin
from .models import contact_us


# Register your models here.

class contact_usadmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website', 'message')


admin.site.register(contact_us, contact_usadmin)
