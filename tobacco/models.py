# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Tobacco(models.Model):
    class Meta():
        db_table = "tobacco"
        unique_together = (('brand', 'taste'),)
    brand = models.CharField(max_length = 200)
    taste_kind = models.CharField(max_length = 200)
    taste = models.CharField(max_length = 200)    
    img_src = models.URLField()

class Tobacco_rating(models.Model):
    class Meta():
        db_table = "tobacco_rating"
        unique_together = (('tobacco_id', 'user_id'),)
    tobacco_id = models.ForeignKey(Tobacco)
    user_id = models.ForeignKey(User)    
    rating = models.IntegerField()

class Tobacco_coments(models.Model):
    class Meta():
        db_table = 'tobacco_coments'
    user = models.ForeignKey(User)
    text = models.TextField()
    tobacco = models.ForeignKey(Tobacco)
    date = models.DateTimeField(default = '1970-01-01 00:00:00')    