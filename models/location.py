from django.db import models


class LocationLog(models.Model):
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
