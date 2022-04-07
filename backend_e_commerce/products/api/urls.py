from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.api.views import ProductsApiViewSet

router = DefaultRouter()
router.register(r'products', ProductsApiViewSet, basename="products")
app_name = 'products'
urlpatterns = [
    path('/', include(router.urls))
]
