from rest_framework import serializers
from .models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = NetworkNode
        fields = ('id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'created_at',
                  'products')
        read_only_fields = ('debt',)

    def update(self, instance, validated_data):
        """Запрещает обновление 'debt' через API"""
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)
