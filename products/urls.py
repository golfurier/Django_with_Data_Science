from django.urls import path
from .views import add_purchase_view, chart_select_view

app_name = 'products'

urlpatterns = [
    path('', chart_select_view, name='main-product-view'),
    path('add/', add_purchase_view, name='add-purchase-view')
]