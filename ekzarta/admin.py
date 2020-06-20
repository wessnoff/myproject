from django.contrib import admin

from .models import Employee, Contacts, Reviews

# Register your models here.
admin.site.register(Employee)
admin.site.register(Contacts)
admin.site.register(Reviews)
