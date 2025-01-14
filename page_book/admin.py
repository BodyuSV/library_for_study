from tkinter.font import names

from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'photo', 'file', 'time_create', 'is_published', 'cat',)
    list_display_links = ('title','content', 'photo', 'file', 'time_create', 'cat',)
    search_fields = ('title','content', 'photo', 'file', 'time_create', 'cat',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'cat',)

admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')
    list_display_links = ('name')
    search_fields = ('name')


admin.site.register(Category)