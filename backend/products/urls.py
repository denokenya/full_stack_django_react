from django.db import router


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

#import Product_ViewSet
from products.api.views.product_view import Product_ViewSet

router = DefaultRouter()
router.register("products", Product_ViewSet, "products")



urlpatterns = [
    path('api/token', obtain_auth_token, name='api-token'),
    path('', include(router.urls)),
]
