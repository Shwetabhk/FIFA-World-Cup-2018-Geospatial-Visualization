from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    image = models.CharField(max_length=1000, null=True)


class Team(models.Model):
    name = models.CharField(max_length=30, null=False)
    fifacode = models.CharField(max_length=30, null=False)
    iso2 = models.CharField(max_length=30, null=False)
    flag = models.CharField(max_length=1000, null=True)
    latitude = models.FloatField(null=False, default=0)
    longitude = models.FloatField(null=False, default=0)


class Channel(models.Model):
    name = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    language = models.CharField(max_length=30, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    icon = models.CharField(max_length=1000, null=True)
