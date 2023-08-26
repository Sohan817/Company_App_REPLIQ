from django.db import models

# Create your models here.
class AddEmployee(models.Model):
    name = models.CharField(max_length=30)
    employee_id = models.CharField(max_length=30)