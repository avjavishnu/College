from django.db import models
import datetime


class StudentPlacements(models.Model):
    studentId = models.CharField(max_length=30, null=False)
    companyName = models.CharField(max_length=50, null=False)
    selectedRole = models.CharField(max_length=50, null=False)
    salaryPackage = models.FloatField(null=False)
    internship = models.BooleanField(default=False)
    createdOn = models.DateTimeField(default=datetime.datetime.now())


class Internship(models.Model):
    studentId = models.CharField(max_length=30, null=False)
    companyName = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=False)
    stipend = models.FloatField(null=False)
    createdOn = models.DateTimeField(default=datetime.datetime.now())
