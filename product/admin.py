from django.contrib import admin
from .models import Product, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'price', 'available', 'created_at']
    list_editable = ['price', 'available']
    summernote_fields = '__all__'





admin.site.register(Category)