from django.shortcuts import render
from django.urls import path, reverse_lazy
from .views import AuthView, CustomPasswordResetView, CustomPasswordResetConfirmView, LogoutView, ProfileView


urlpatterns = [
    path('auth/', AuthView.as_view(), name='authenticated'),
    path('auth/<str:form>', AuthView.as_view(), name='login_register'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('profile/info', ProfileView.as_view(), name='profile'),
    
    # Password Reset urls
    path('reset/password/', CustomPasswordResetView.as_view(), name='forgot_password'),
    path('reset/password/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]