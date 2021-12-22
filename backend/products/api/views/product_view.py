
import django_filters.rest_framework
#import ModelViewSet
from rest_framework.viewsets import ModelViewSet

#import product serializer
from products.api.serializers.product_serializer import Product_Serializer
#import product model
from products.models.product_model import Product

from mixins .apimixin import DefaultMixin


class Product_ViewSet(ModelViewSet):

    """Product API End points."""
    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    search_fields = ('title',)
    ordering = ('title',)
