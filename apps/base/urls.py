from django.urls import path
from ..base.views import PartnerListView, PartnerDetailView, PartnerCreateView, PartnerUpdateView, DeletePartner
from ..base.views import CompanyListView
from ..base.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, DeleteProduct

urlpatterns = [
    path('products', ProductListView.as_view(), name='products'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('Product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('Product/<int:pk>/delete/', DeleteProduct, name='product-delete'),

    path('companies', CompanyListView.as_view(), name='companies'),

    path('partners', PartnerListView.as_view(), name='partners'),
    path('partner/add/', PartnerCreateView.as_view(), name='partner-add'),
    path('partner/<int:pk>/', PartnerDetailView.as_view(), name='partner-detail'),
    path('partner/<int:pk>/update', PartnerUpdateView.as_view(), name='partner-update'),
    path('partner/<int:pk>/delete/', DeletePartner, name='partner-delete'),
]
