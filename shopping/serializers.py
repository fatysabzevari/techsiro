from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    This serializer is responsible for converting Product model instances into
    JSON representations and vice versa. It utilizes the ModelSerializer class
    provided by Django Rest Framework for automatic serialization and deserialization
    of Product instances.

    Attributes:
        model: The Product model class associated with this serializer.
        fields: A list of fields to include in the serialized representation ('__all__' for all fields).

    """
    class Meta:
        model = Product
        fields = '__all__'
