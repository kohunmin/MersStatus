from django.contrib import admin

# Register your models here.
from .models import mersStatus

class mersStatusAdmin(admin.ModelAdmin):
    fields = ['coughStatus','breathingStatus','temperature','pub_date']

admin.site.register(mersStatus)