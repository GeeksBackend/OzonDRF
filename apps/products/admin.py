from django.contrib import admin

from apps.products.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'created')
    search_fields = ('title', 'description', 'price')
    list_filter = ('shop__title', )

# admin.site.register(Product)