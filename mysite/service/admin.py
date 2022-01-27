from django.contrib import admin
from .models import Category, Item, Staff
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'position', 'available']
    list_filter = ['available']
    list_editable = ['position', 'available']
    prepopulated_fields = {'slug': ('name',)}