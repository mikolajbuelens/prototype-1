from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'source', 'image')

admin.site.register(Article, ArticleAdmin)