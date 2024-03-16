from django.contrib import admin
from .models import TodoItem

# Register your models here.
class MyAdminItem(admin.ModelAdmin):
    list_display=('title','completed','created_at')

admin.site.register(TodoItem,MyAdminItem)