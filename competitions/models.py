from django.db import models


class buyers(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)


class competitions(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    buyer = models.ForeignKey(buyers, unique=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    open = models.DateTimeField()
    closed = models.DateTimeField()
    minimum_capacity = models.IntegerField()
    currency = models.CharField(max_length=3)


class sellers(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    verified = models.BooleanField(null=True, blank=True)


class bids(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    created = models.DateTimeField()
    accepted = models.BooleanField(null=True, blank=True)
    competition = models.ForeignKey(competitions, on_delete=models.CASCADE, unique=False, null=True, blank=True)
    seller = models.ForeignKey(sellers, on_delete=models.CASCADE, unique=False, null=True, blank=True)
    value = models.FloatField()
    offered_capacity = models.IntegerField()
