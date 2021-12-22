from django.db import models

from datetime import datetime


class Product(models.Model):
    """
        Model containing product information
    """
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "products"
        ordering = ["title"]
        verbose_name = "product"
        verbose_name_plural = "products"
