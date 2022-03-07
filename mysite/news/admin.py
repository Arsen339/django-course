from django.contrib import admin
from .models import News, Category
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    """представление выходных данных в админке"""
    list_display = ("id", "title", "created_at","category", "updated_at", "is_published")
    # сделаем поля ссылками
    list_display_links = ("id", "title")
    # поля для поиска
    search_fields = ("title", "content")
    list_editable = ("is_published", "category")

class CategoryAdmin(admin.ModelAdmin):
    """представление выходных данных в админке"""
    list_display = ("id", "title")
    # сделаем поля ссылками
    list_display_links = ("id", "title")
    # поля для поиска
    search_fields = ("title",)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)