from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Item, Category, ItemImage, UserProfile
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

# Register your models here.



class ItemImageInline(admin.TabularInline):
    model = ItemImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, obj):
        return format_html('<img src="{}" width="150" height="150">', obj.image.url)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'condition', 'seller', 'category']
    inlines = [ItemImageInline]
    list_editable = ['price']
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'inventory_count']

    @admin.display(ordering='inventory_count')
    def inventory_count(self, category):
        url = (
            reverse('admin:store_item_changelist')
            + '?'
            + urlencode({
                'category__id': str(category.id)
            })
               
        )
        return format_html("<a href='{}'>{}</a>",url, category.inventory_count)
        
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            inventory_count=Count('item')
        )
    

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'inventory_count']
#     def inventory_count(self, items):
#         return Item.objects.filter(category=items).count()
    
    inventory_count.short_description = 'Products In each Category'  # Customizes the column header

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone']
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    


admin.site.register(ItemImage)





