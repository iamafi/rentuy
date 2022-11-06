from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import ProfileView

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', ProfileView.as_view(), name='profile')
]
