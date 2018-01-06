from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=3, max_digits=10, default=0.00)

    def __str__(self):
        return self.name
