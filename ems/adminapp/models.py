from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.SmallIntegerField()
    class Meta:
        db_table = 'userdb'
