from django.db import models

# Create your models here.
class Device(models.Model):
    employee_id = models.CharField(max_length=30)
    employee_name = models.CharField(max_length=30)
    device_name = models.CharField(max_length=30)
    issue_date = models.CharField(max_length=30)
    return_date = models.CharField(max_length=30)