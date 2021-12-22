from django.db.models import fields
from rest_framework import serializers

from products.models.product_model import Product




class Product_Serializer(serializers.ModelSerializer):
    """
        List information of the Product:
          title,
          price,




    """
  

    class Meta:

        model = Product
        fields = [

            'id',
            'title',
            'price',
        ]
        read_only_fields =['id',]
        
