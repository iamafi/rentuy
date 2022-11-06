from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, get_object_or_404

from account.models import User
from account.serializers import ProfileSerializer


class ProfileView(RetrieveAPIView, LoginRequiredMixin):
    serializer_class = ProfileSerializer

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.pk)
