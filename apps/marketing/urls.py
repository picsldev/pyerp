from django.urls import path
from django.contrib.auth import views as auth_views
from .subviews.channel import ChannelListView, ChannelDetailView, ChannelCreateView, ChannelUpdateView, DeleteChannel
from .subviews.campaign import CampaignListView, CampaignDetailView, CampaignCreateView, CampaignUpdateView, DeleteCampaign


urlpatterns = [
    path('channel', ChannelListView.as_view(), name='channel'),
    path('channel/add/', ChannelCreateView.as_view(), name='channel-add'),
    path('channel/<int:pk>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('channel/<int:pk>/update', ChannelUpdateView.as_view(), name='channel-update'),
    path('channel/<int:pk>/delete/', DeleteChannel, name='channel-delete'),

    path('campaign', CampaignListView.as_view(), name='campaign'),
    path('campaign/add/', CampaignCreateView.as_view(), name='campaign-add'),
    path('campaign/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    path('campaign/<int:pk>/update', CampaignUpdateView.as_view(), name='campaign-update'),
    path('campaign/<int:pk>/delete/', DeleteCampaign, name='campaign-delete'),
]