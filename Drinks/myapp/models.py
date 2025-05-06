from django.db import models

# Create your models here.

class Beverages(models.Model):
    name = models.CharField(max_length=20)
    flavour = models.CharField(max_length=30)


    def __str__(self):
        return self.name
