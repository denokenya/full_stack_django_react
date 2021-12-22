"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/', include('products.urls')),

    # path('api/', include('student.urls')),
    path('api/auth/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('rest_framework.urls')),
    path('schema/', get_schema_view(
        title="Shopping Cart API",
        description="API for the Shopping Cart APP",
        version="1.0.0"
    ), name="shoppingcart-schema"),
    path('', include_docs_urls(
        title="Shopping Cart API",
        description="API for the Shopping Cart APP",
    ), name="shoppingcart-docs")

]
admin.site.site_header = "Shopping Cart ERP Admin Area"
admin.site.site_title = "Shopping Cart ERP"
admin.site.index_title = "Shopping Cart Administration"
