from rest_framework import serializers
from .models import Order, OrderItem
from ..product.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Assuming ProductSerializer is defined

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'created_at', 'updated_at', 'items')
        read_only_fields = ('user', 'created_at', 'updated_at')
