from django.contrib import admin

from .models import Sneaker, Brand, Category, Size


class SizeInline(admin.TabularInline):
    model = Size
    extra = 0


class SneakerAdmin(admin.ModelAdmin):
    inlines = [SizeInline]
    list_display = ('__str__', 'cost', 'vendor_code', 'color')


admin.site.register(Sneaker, SneakerAdmin)
admin.site.register(Brand)
admin.site.register(Category)

