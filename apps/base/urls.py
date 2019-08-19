from django.urls import path
from django.contrib.auth import views as auth_views
from ..base.views import CustomerListView, PartnerDetailView, PartnerCreateView, PartnerUpdateView, DeletePartner, ProviderListView
from ..base.views import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, DeleteCompany
from .subviews.product import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, DeleteProduct
from ..base.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, DeleteUser, ChangePasswordForm, DoChangePassword
from .subviews.product_category import ProductCategoryListView, ProductCategoryDetailView, ProductCategoryCreateView, ProductCategoryUpdateView, DeleteProductCategory
from ..base.views import UpdateBaseConfigView

urlpatterns = [
    path('config/<int:pk>', UpdateBaseConfigView.as_view(), name='base-config'),

    path('users', UserListView.as_view(), name='users'),
    path('user/add/', UserCreateView.as_view(), name='user-add'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', DeleteUser, name='user-delete'),
    path('user/change-password/<int:pk>', ChangePasswordForm, name='password-change'),
    path('user/change-password-confirm/<int:pk>', DoChangePassword, name='do-change-password'),

    path('products', ProductListView.as_view(), name='products'),
    path('product/add/', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('Product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('Product/<int:pk>/delete/', DeleteProduct, name='product-delete'),

    path('companies', CompanyListView.as_view(), name='companies'),
    path('company/add/', CompanyCreateView.as_view(), name='company-add'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('company/<int:pk>/update', CompanyUpdateView.as_view(), name='company-update'),
    path('company/<int:pk>/delete/', DeleteCompany, name='company-delete'),

    path('partners', CustomerListView.as_view(), name='partners'),
    path('provider', ProviderListView.as_view(), name='provider'),

    path('partner/add/', PartnerCreateView.as_view(), name='partner-add'),
    path('partner/<int:pk>/', PartnerDetailView.as_view(), name='partner-detail'),
    path('partner/<int:pk>/update', PartnerUpdateView.as_view(), name='partner-update'),
    path('partner/<int:pk>/delete/', DeletePartner, name='partner-delete'),

    path('product-category', ProductCategoryListView.as_view(), name='product-category'),
    path('product-category/add/', ProductCategoryCreateView.as_view(), name='product-category-add'),
    path('product-category/<int:pk>/', ProductCategoryDetailView.as_view(), name='product-category-detail'),
    path('product-category/<int:pk>/update', ProductCategoryUpdateView.as_view(), name='product-category-update'),
    path('product-category/<int:pk>/delete/', DeleteProductCategory, name='product-category-delete'),
]
