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


class Ship(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    manufactureTime = models.CharField(max_length=255)
    manufactureDress = models.CharField(max_length=255)
    flag = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    port = models.CharField(max_length=255)
    tonnageTotal = models.CharField(max_length=255)
    tonnageNet = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    power = models.CharField(max_length=255)
    location = models.CharField(max_length=255)