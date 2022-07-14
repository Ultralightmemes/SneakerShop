from django.contrib import admin

from .models import Sneaker, Brand, Category, Size

admin.site.register(Sneaker)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Size)

