from django.db import models


class Operation(models.Model):
    name = models.CharField(max_length=12, null=True)


class Bin(models.Model):
    operation = models.ManyToManyField(Operation)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    collection_frequency = models.IntegerField(null=True)
    last_collection = models.DateTimeField(null=True)
