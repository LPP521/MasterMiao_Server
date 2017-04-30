from django.db import models


class LocationLog(models.Model):
    date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
