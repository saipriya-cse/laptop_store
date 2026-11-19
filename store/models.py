
from django.db import models


class Laptop(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    ram = models.CharField(max_length=20)
    storage = models.CharField(max_length=50)
    processor = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='laptops/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
