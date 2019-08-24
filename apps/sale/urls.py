from django.urls import path
from .subviews.saleorder import SaleOrderListView


urlpatterns = [
    path('sale-order', SaleOrderListView.as_view(), name='sale-order'),
    path('sale-order/add/', SaleOrderListView.as_view(), name='sale-order-add'),
]
