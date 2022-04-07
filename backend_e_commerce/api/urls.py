from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('products', include('products.api.urls', namespace='products')),
    path('categories', include('categories.api.urls', namespace='categories')),
    path('invoices', include('invoices.api.urls', namespace='invoices')),
    path('offers', include('offers.api.urls', namespace='offers'))
]

