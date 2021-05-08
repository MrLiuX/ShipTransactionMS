from django.db import models

class Personnel(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    mobileNumber = models.CharField(max_length=11)
    teleNumber = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    department = models.ForeignKey(
        "Department", on_delete=models.CASCADE)


class Department(models.Model):
    department = models.CharField(max_length=255, primary_key=True)
    minister = models.CharField(max_length=255, default="none")
    note = models.CharField(max_length=255, default="无")
