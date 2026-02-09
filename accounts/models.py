from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)