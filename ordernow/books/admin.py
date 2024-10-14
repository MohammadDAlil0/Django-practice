from django.contrib import admin
from .models import Inventory


class InverntoryAdmin(admin.ModelAdmin):
    list_display = ("title", "quantity", "price", "title")

# Register your models here.
admin.site.register(Inventory, InverntoryAdmin)