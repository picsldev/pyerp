from django.urls import path
from ..base.views import PartnerListView, CompanyListView

urlpatterns = [
    path('partners', PartnerListView.as_view()),
    path('companies', CompanyListView.as_view()),
]
