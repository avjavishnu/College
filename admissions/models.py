from django.db import models
import datetime


class AdmissionSection(models.Model):
    sectionId = models.CharField(max_length=20, null=False)
    sectionName = models.CharField(max_length=50, null=False)
    numberOfEmployees = models.IntegerField(null=False)


class Employee(models.Model):
    empId = models.CharField(max_length=20, null=False)
    empName = models.CharField(max_length=50, null=False)
    departmentId = models.CharField(max_length=20, null=False)
    empDesignation = models.CharField(max_length=30, null=False)
    experience = models.CharField(max_length=20, null=False)
    dateOfBirth = models.DateField(null=False)
    gender = models.CharField(max_length=10, null=False)
    bloodGroup = models.CharField(max_length=10, null=False)
    addressLine1 = models.CharField(max_length=100, null=False)
    addressLine2 = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=50, null=False)
    pincode = models.CharField(max_length=100, null=False)
    degree = models.CharField(max_length=50, null=False)
    createdOn = models.DateTimeField(default=datetime.datetime.now())
    isActive = models.BooleanField(default=True)


class Student(models.Model):
    studentId = models.CharField(max_length=20, null=False)
    studentName = models.CharField(max_length=50, null=False)
    departmentId = models.CharField(max_length=20, null=False)
    dateOfBirth = models.DateField(null=False)
    gender = models.CharField(max_length=10, null=False)
    bloodGroup = models.CharField(max_length=10, null=False)
    addressLine1 = models.CharField(max_length=100, null=False)
    addressLine2 = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=50, null=False)
    pincode = models.CharField(max_length=100, null=False)
    degree = models.CharField(max_length=50, null=False)
    marks = models.CharField(max_length=15, null=False)
    createdOn = models.DateTimeField(default=datetime.datetime.now())
    isActive = models.BooleanField(default=True)
