# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = "article"
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField(default = '1970-01-01 00:00:00')
    article_likes = models.IntegerField(default = 0)

class Comments(models.Model):
    class Meta():
        db_table = 'Comments'
    comments_user = models.ForeignKey(User)
    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)
    comments_date = models.DateTimeField(default = '1970-01-01 00:00:00')