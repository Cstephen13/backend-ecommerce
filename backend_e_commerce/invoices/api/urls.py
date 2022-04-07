from django.urls import path, include
from rest_framework.routers import DefaultRouter

from invoices.api.views import InvoiceApiViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceApiViewSet, basename="invoices")
app_name = 'invoices'
urlpatterns = [
    path('/', include(router.urls))
]
