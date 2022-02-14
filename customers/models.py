from django.db import models

# Create your models here.
class Customer():
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

