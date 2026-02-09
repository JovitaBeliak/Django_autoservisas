from django.contrib import admin
from .models import Service, Car, Order, OrderLine, OrderReview

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    can_delete = False
    extra = 0
    fields = ["service", "quantity", "line_sum"]
    readonly_fields = ["line_sum"]

class OrderReviewInLine(admin.TabularInline):
    model = OrderReview
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ["car", "client", "date", "status", "due_date", "total"]
    list_filter = ["car", "date", "status", "due_date", "client"]
    list_editable = ["status", "due_date", "client"]
    inlines = [OrderLineInline, OrderReviewInLine]
    readonly_fields = ["date", "total"]

    fieldsets = [
        ("General", {"fields": ["car", "client", "date", "status", "due_date", "total"]})
    ]

class CarAdmin(admin.ModelAdmin):
    list_display = ["make", "model", "client_name", "license_plate", "vin_code"]
    list_filter = ["client_name", "make", "model"]
    search_fields = ["license_plate", "vin_code"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]

class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ["order", "reviewer", "date_created", "content"]



# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
admin.site.register(OrderReview, OrderReviewAdmin)