# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Article,Comments

# Register your models here.
class ArticleInline(admin.StackedInline):
    model =  Comments
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','article_title', 'article_date')
    exclude = ['article_likes']
    inlines = [ArticleInline]
    list_filter = ['article_date']

admin.site.register(Article, ArticleAdmin)