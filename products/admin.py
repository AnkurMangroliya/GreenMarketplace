from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'seller', 'date_added')
    search_fields = ('name', 'description')
    list_filter = ('category', 'date_added')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
