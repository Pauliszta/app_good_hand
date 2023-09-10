from django.contrib import admin

# Register your models here.

from .models import Donation, Institution, Category

admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Donation)
