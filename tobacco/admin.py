# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tobacco.models import Tobacco


class TobaccoAdmin(admin.ModelAdmin):
    list_display = ('id','brand', 'taste_kind', 'taste', 'img_src')
# Register your models here.
admin.site.register(Tobacco,TobaccoAdmin)