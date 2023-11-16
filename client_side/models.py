from django.db import models

from shop_side.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f"{self.product.name} - {self.username}"






