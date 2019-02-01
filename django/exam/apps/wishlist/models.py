# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	datehired = models.DateTimeField()
	
class Item(models.Model):
	name = models.CharField(max_length=255)
	created_by = models.ForeignKey(User, related_name="items")
	
class Wishlist(models.Model):
	users = models.ForeignKey(User, related_name="wishlists")
	items = models.ForeignKey(Item, related_name = "wishlists")
	created_at = models.DateTimeField(auto_now_add = True)
	