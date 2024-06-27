from .models import Order, OrderItem
from .serializers import OrderSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from ..cart.models import Cart


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        cart_items = self.get_cart_items(request.user)

        if not cart_items:
            return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        # Create an order from cart items
        order_serializer = self.get_serializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order = order_serializer.save(user=request.user)

        # Create order items from cart items and delete cart items
        for cart_item in cart_items:
            OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity)
            cart_item.delete()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

    def get_cart_items(self, user):
        # Method to retrieve and return cart items for the given user
        return Cart.objects.filter(user=user)

    def update(self, request, *args, **kwargs):
        return Response({"error": "Method 'PATCH' not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"error": "Method 'PATCH' not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



