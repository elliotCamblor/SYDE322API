from __future__ import unicode_literals

from django.db import models

class Players(models.Model):
    playerId = models.CharField(max_length=200)
    lastSession = models.DateTimeField('Last Session')
    joinedDate = models.DateTimeField('Joined Date')
    rank = models.IntegerField()

class Settings(models.Model):
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    # insert all of our settings here #

class Cars(models.Model):
	player = models.ForeignKey(Players, on_delete=models.CASCADE)
	carModel = models.CharField(max_length=200)
	colour = models.CharField(max_length=200)
	isActive = models.BooleanField()
