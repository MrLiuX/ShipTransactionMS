from django.db import models

# Create your models here.


class Personnel(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mobileNumber = models.CharField(max_length=11)
    teleNumber = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    department = models.ForeignKey(
        "Department", on_delete=models.CASCADE)

class Department(models.Model):
    department = models.CharField(max_length=255)
