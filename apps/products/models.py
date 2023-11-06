from django.db import models

from apps.shops.models import Shop

# Create your models here.
class Product(models.Model):
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE,
        related_name="shop_products",
        verbose_name="Магазин"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        max_length=500,
        verbose_name="Описание",
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to="product_image/",
        verbose_name="Фотография"
    )
    price = models.IntegerField(
        verbose_name="Цена"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"