from django.urls import path, include
from rest_framework.routers import DefaultRouter

from offers.api.views import OfferApiViewSet

router = DefaultRouter()
router.register(r'offers', OfferApiViewSet, basename="offers")
app_name = 'offers'
urlpatterns = [
    path('/', include(router.urls))
]
