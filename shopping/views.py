import logging  # Import the logging module
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create a logger for this view
logger = logging.getLogger(__name__)

class ProductCreateView(generics.CreateAPIView):
    """
    API endpoint for creating a new product.

    This view allows authenticated users to create a new product by providing
    the necessary data in the request payload.

    Attributes:
        serializer_class (Serializer): The serializer class used for validation and serialization.
        permission_classes (list of classes): The list of permission classes applied to this view.

    Methods:
        create(request, *args, **kwargs):
            Create a new product using the provided data in the request payload.

    Raises:
        HTTP 400 Bad Request: If there are validation errors or an exception occurs during product creation.

    Returns:
        HTTP 201 Created: If the product is successfully created, the created product data is returned.
    """
    serializer_class = ProductSerializer  # Serializer for product data
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication

    def create(self, request, *args, **kwargs):
        """
        Create a new product using the provided data in the request payload.

        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)  # Validate product data
            serializer.save()  # Save the product to the database
            logger.info("Product created successfully.")  # Log a success message
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with created product data
        except Exception as e:
            logger.error(f"Error creating product: {str(e)}")  # Log an error message
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)  # Respond with an error message if an exception occurs
