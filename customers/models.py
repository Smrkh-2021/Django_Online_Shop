from django.db import models

# Create your models here.
class Customer():
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)