from django.contrib import admin

from .models import Order, Basket


class SizeInline(admin.TabularInline):
    model = Order
    extra = 0


class BasketAdmin(admin.ModelAdmin):
    inlines = [SizeInline]


admin.site.register(Order)
admin.site.register(Basket, BasketAdmin)
# Register your models here.
