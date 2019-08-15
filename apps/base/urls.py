from django.urls import path
from ..base.views import PartnerListView, PartnerCreateView, PartnerUpdateView, PartnerDeleteView, CompanyListView, ProductListView

urlpatterns = [
    path('partners', PartnerListView.as_view()),
    path('products', ProductListView.as_view()),
    path('companies', CompanyListView.as_view()),

    path('partner/add/', PartnerCreateView.as_view(), name='partner-add'),
    path('partner/<int:pk>/', PartnerUpdateView.as_view(), name='partner-update'),
    path('partner/<int:pk>/delete/', PartnerDeleteView.as_view(), name='partner-delete'),

]
