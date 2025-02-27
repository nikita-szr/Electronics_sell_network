from django.contrib import admin
from .models import NetworkNode, Product


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'supplier', 'debt')
    list_filter = ('city',)
    search_fields = ('name', 'city')
    raw_id_fields = ('supplier',)
    inlines = [ProductInline]
    actions = [clear_debt]

    def get_hierarchy_level(self, obj):
        return obj.get_hierarchy_level()

    get_hierarchy_level.short_description = "Уровень в сети"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
