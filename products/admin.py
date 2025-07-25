from django.contrib import admin

# Register your models here.
from .models import Category, Product, File

#How to register:
    #method 1:
# admin.site.register(Product)

#method 2:
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'is_enable']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']
    
class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file' ,'is_enable']
    extra = 0
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [FileInlineAdmin]
    