from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    salary = models.CharField(max_length=20)
    headpic = models.ImageField(upload_to='pics')
    class Meta:
        db_table = 'emplist'
