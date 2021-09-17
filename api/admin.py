from django.contrib import admin

from .models import Product, Parameter, ParametersItem


class ParameterInline(admin.TabularInline):
    model = ParametersItem
    fields = ["product_title", "parameter_title"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_title",
        "description",
    )
    search_fields = ("product_title",)
    list_filter = ("product_title",)
    empty_value_display = "-пусто-"
    inlines = [ParameterInline]


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(ParametersItem)
class ParametersItemAdmin(admin.ModelAdmin):
    list_display = (
        "product_title",
        "parameter_title",
    )
    list_display_links = ("product_title", "parameter_title")
    list_filter = (
        "product_title",
        "parameter_title",
    )