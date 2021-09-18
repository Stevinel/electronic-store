from django.db import models


class Product(models.Model):
    """Модель товара/продукта"""

    product_title = models.CharField("Название", max_length=50)
    description = models.CharField("Описание", max_length=3000)
    parameter = models.ManyToManyField("Parameter", through="ParametersItem")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.product_title


class Parameter(models.Model):
    """Модель параметра продукта"""

    title = models.CharField("Название параметра", max_length=100, unique=True)

    class Meta:
        verbose_name = "Параметр"
        verbose_name_plural = "Параметры"

    def __str__(self):
        return self.title


class ParametersItem(models.Model):
    """Модель связывающая отношение manytomany, продукта и параметра"""

    product_title = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_parameters",
        verbose_name="Название товара",
    )
    parameter_title = models.ForeignKey(
        Parameter,
        on_delete=models.CASCADE,
        related_name="parameters",
        verbose_name="Параметры товара",
    )

    class Meta:
        verbose_name = "Параметр итем"
        verbose_name_plural = "Параметр итемы"

    def __str__(self):
        return (
            f"{self.product_title.product_title} {self.parameter_title.title}"
        )
