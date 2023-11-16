from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    created_at = models.DateField(auto_now_add=True)
    shop = models.ManyToManyField('Shop', blank=True)
    slug = models.SlugField(max_length=255,
                            blank=True,
                            unique=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f"{self.name}-{self.price}")
        return super().save()

    def __str__(self):
        return f"{self.name} - {self.price}"


class Shop(models.Model):
    title = models.CharField('Shop title', max_length=255)
    address = models.CharField('Address', max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.title, self.address)






