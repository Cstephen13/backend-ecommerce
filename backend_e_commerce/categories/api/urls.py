from django.urls import path, include
from rest_framework.routers import DefaultRouter
from categories.api.views import CategoryApiViewSet

router = DefaultRouter()
router.register(r'categories', CategoryApiViewSet, basename="categories")
app_name = 'categories'
urlpatterns = [
    path('/', include(router.urls))
]
