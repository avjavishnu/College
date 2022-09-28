from django.db import models
import datetime


class Driver(models.Model):
    driverId = models.CharField(max_length=30, null=False)
    driverName = models.CharField(max_length=50, null=False)
    salaryPackage = models.FloatField(null=False)
    createdOn = models.DateTimeField(default=datetime.datetime.now())
