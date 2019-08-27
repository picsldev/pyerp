from django.urls import path
from django.contrib.auth import views as auth_views
from .subviews.post import PostListView, PostDetailView, PostCreateView, PostUpdateView, DeletePost
from .subviews.website_config import UpdateWebsiteConfigView
from .subviews.web_payment_method import WebPaymentMethodListView, WebPaymentMethodDetailView, WebPaymentMethodCreateView, WebPaymentMethodUpdateView, DeleteWebPaymentMethod


urlpatterns = [
    path('post', PostListView.as_view(), name='post'),
    path('post/add/', PostCreateView.as_view(), name='post-add'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletePost, name='post-delete'),

    path('config/<int:pk>', UpdateWebsiteConfigView.as_view(), name='website-config'),

    path('web-payment-methods', WebPaymentMethodListView.as_view(), name='web-payment-methods'),
    path('web-payment-method/add/', WebPaymentMethodCreateView.as_view(), name='web-payment-method-add'),
    path('web-payment-method/<int:pk>/', WebPaymentMethodDetailView.as_view(), name='web-payment-method-detail'),
    path('web-payment-method/<int:pk>/update', WebPaymentMethodUpdateView.as_view(), name='web-payment-method-update'),
    path('web-payment-method/<int:pk>/delete/', DeleteWebPaymentMethod, name='web-payment-method-delete'),
]