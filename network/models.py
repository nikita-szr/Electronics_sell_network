from django.db import models
from django.core.exceptions import ValidationError


class NetworkNode(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")
    supplier = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='clients', verbose_name="Поставщик"
    )
    debt = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Задолженность"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ['id']
        verbose_name = "Узел сети"
        verbose_name_plural = "Узлы сети"

    def __str__(self):
        return self.name

    def get_hierarchy_level(self):
        """Определяет уровень в иерархии по цепочке поставщиков"""
        level = 0
        supplier = self.supplier
        while supplier:
            level += 1
            supplier = supplier.supplier
        return level

    def clean(self):
        """Запрещает указывать поставщика с тем же или большим уровнем"""
        if self.supplier and self.get_hierarchy_level() <= self.supplier.get_hierarchy_level():
            raise ValidationError("Поставщик должен находиться выше в иерархии.")


class Product(models.Model):
    network_node = models.ForeignKey(
        NetworkNode, on_delete=models.CASCADE, related_name='products', verbose_name="Торговая точка"
    )
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    class Meta:
        ordering = ['-release_date']
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} ({self.model})"
