from django.urls import path
from ..base.views import PartnerListView, PartnerDetailView, PartnerCreateView, PartnerUpdateView, DeletePartner
from ..base.views import CompanyListView
from ..base.views import ProductListView

urlpatterns = [
    path('partners', PartnerListView.as_view(), name='partners'),
    path('products', ProductListView.as_view()),
    path('companies', CompanyListView.as_view()),

    path('partner/add/', PartnerCreateView.as_view(), name='partner-add'),
    path('partner/<int:pk>/', PartnerDetailView.as_view(), name='partner-detail'),
    path('partner/<int:pk>/update', PartnerUpdateView.as_view(), name='partner-update'),
    path('partner/<int:pk>/delete/', DeletePartner, name='partner-delete'),
]
