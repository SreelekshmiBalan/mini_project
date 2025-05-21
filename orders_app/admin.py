from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'created_at', 'is_paid')
    list_filter = ('status', 'is_paid', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]
    list_editable = ('status',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'size', 'price')
