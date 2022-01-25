from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'table_id', 'room', 'paid',
                    'created', 'updated', 'served']
    list_filter = ['served', 'paid', 'created', 'updated']
    inlines = [OrderItemInline]

