from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404, CreateAPIView

from property.models import Property, Review
from property.serializers import PropertyListSerializer, PropertyDetailSerializer, ReviewSerializer, RequestSerializer


class PropertyListView(ListAPIView, LoginRequiredMixin):
    serializer_class = PropertyListSerializer

    def get_queryset(self):
        qs = Property.objects.filter(renter=None).order_by('-created')
        if 'recommended' in self.request.GET:
            return qs.filter(recommended=True)
        if 'district' in self.request.GET:
            qs = qs.filter(district__in=self.request.GET.get('district'))
        if 'rooms' in self.request.GET:
            qs = qs.filter(rooms__gte=int(self.request.GET.get('rooms')))
        if 'pets' in self.request.GET:
            qs = qs.filter(pets=True)
        if 'long_term' in self.request.GET:
            qs = qs.filter(long_term=True)
        if 'verified' in self.request.GET:
            qs = qs.filter(verified=True)
        return qs


class PropertyDetailView(RetrieveAPIView, LoginRequiredMixin):
    serializer_class = PropertyDetailSerializer
    queryset = Property.objects.filter(renter=None).order_by('-created')

    def get_object(self):
        return get_object_or_404(Property, id=self.kwargs['pk'])


class ReviewListView(ListAPIView, LoginRequiredMixin):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()


class RequestCreateView(CreateAPIView, LoginRequiredMixin):
    serializer_class = RequestSerializer
