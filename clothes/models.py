from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Clothing(models.Model):
    name = models.CharField(max_length=100)
    purchaser = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name
