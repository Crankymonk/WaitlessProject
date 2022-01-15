from django.contrib import admin
from .models import Category, Item
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price']
    # list_filter = ['available', 'created', 'updated']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}