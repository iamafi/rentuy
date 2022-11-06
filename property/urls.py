from django.urls import path

from property.views import PropertyListView, PropertyDetailView, ReviewListView, RequestCreateView

urlpatterns = [
    path('list', PropertyListView.as_view(), name='property-list'),
    path('details/<int:pk>', PropertyDetailView.as_view(), name='property-details'),
    path('details/<int:pk>/review/list', ReviewListView.as_view(), name='review-list'),
    path('request/create', RequestCreateView.as_view(), name='request-create')
]
