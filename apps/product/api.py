# views.py
from rest_framework import viewsets, status, filters
from .models import Product, Category, ProductImage
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from ..utils.permissions import IsSuperuser
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = (JWTAuthentication,)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsSuperuser()]
        return super().get_permissions()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

    # Define fields for filtering
    filterset_fields = {
        'category': ['exact'],
        'price': ['gte', 'lte'],
        # Add more fields as needed
    }

    # Define fields for searching
    search_fields = ['name', 'description', 'category__name']

    # Define fields for ordering
    ordering_fields = ['name', 'price', 'stock']

    def create(self, request, *args, **kwargs):
        # Extract images from request data
        images_data = request.FILES.getlist('images')  # Assuming images are uploaded as 'images' in form-data

        # Create product instance
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        # Create product images
        for image_data in images_data:
            ProductImage.objects.create(product=product, image=image_data)

        # Serialize response with images included
        product_serializer = ProductSerializer(product, context=self.get_serializer_context())
        return Response(product_serializer.data, status=status.HTTP_201_CREATED)

    # @action(detail=True, methods=['post'], url_path='upload-images')
    # def upload_images(self, request, pk=None):
    #     # Get the product instance
    #     product = self.get_object()
    #
    #     # Extract images from request data
    #     images_data = request.FILES.getlist('images')  # Assuming images are uploaded as 'images' in form-data
    #
    #     # Create product images
    #     for image_data in images_data:
    #         ProductImage.objects.create(product=product, image=image_data)
    #
    #     # Return a success response
    #     return Response({'message': f'Images uploaded successfully for product {product.id}'},
    #                     status=status.HTTP_200_OK)
