from django.db import models

# Create your models here.
class Shop(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название магазина"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание магазина",
        blank=True, null=True
    )
    logo = models.ImageField(
        upload_to='shop_logo/',
        verbose_name="Логотип",
        blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"