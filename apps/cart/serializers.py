from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'product', 'quantity', 'created_at')

    def create(self, validated_data):
        user = self.context['request'].user
        product = validated_data['product']
        existing_cart_item = Cart.objects.filter(user=user, product=product).first()

        if existing_cart_item:
            # If the same product is already in the cart, update its quantity
            existing_cart_item.quantity += validated_data.get('quantity', 1)
            existing_cart_item.save()
            return existing_cart_item
        else:
            # Otherwise, create a new cart item
            validated_data['user'] = user
            cart_item = Cart.objects.create(**validated_data)
            return cart_item

