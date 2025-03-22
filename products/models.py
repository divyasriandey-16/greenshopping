from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=50, unique=True)
    is_eco_friendly = models.BooleanField(default=False)
    alternative = models.CharField(max_length=255, blank=True, null=True)  # Allow manual entry

    def __str__(self):
        return self.name

