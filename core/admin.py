from django.contrib import admin
from .models import Category, City, Ad


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created_at', 'updated_at')
    search_fields = ('title',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'city', 'slug', 'user', 'category', 'price', 'active', 'created_at', 'updated_at')
    search_fields = ('title',)
