from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=100)

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

