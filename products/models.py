from django.db import models
from core.models import BaseModel


# Create your models here.
class Discount(BaseModel):

    type = models.CharField(max_length=20, choices=[('value','Value'),('percent', 'Percent')], null=False)




class Category(BaseModel):
    ...

class Product(BaseModel):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.FileField()
    count = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    dimension = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    properties = models.TextField()
