from django.contrib import admin
from .models import Service, Car, Order, OrderLine

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ["car", "date"]
    inlines = [OrderLineInline]



class CarAdmin(admin.ModelAdmin):
    list_display = ["make", "model", "client_name", "license_plate", "vin_code"]
    list_filter = ["client_name", "make", "model"]
    search_fields = ["license_plate", "vin_code"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ["service"]

# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)