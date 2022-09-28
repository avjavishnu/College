from django.db import models
import datetime


class Department(models.Model):
    departmentId = models.CharField(max_length=15, null=False)
    departmentName = models.CharField(max_length=50, null=False)
    intake = models.IntegerField(null=False)
    createdOn = models.DateTimeField(default=datetime.datetime.now())


class Faculty(models.Model):
    facultyId = models.CharField(max_length=15, null=False)
    facultyName = models.CharField(max_length=50, null=False)
    createdOn = models.DateTimeField(default=datetime.datetime.now())


class Student(models.Model):
    studentId = models.CharField(max_length=15, null=False)
    StudentName = models.CharField(max_length=50, null=False)
    createdOn = models.DateTimeField(default=datetime.datetime.now())


class Lab(models.Model):
    labId = models.CharField(max_length=15, null=False)
    labName = models.CharField(max_length=50, null=False)
    labInCharge = models.CharField(max_length=50, null=False)
    createdOn = models.DateTimeField(default=datetime.datetime.now())
