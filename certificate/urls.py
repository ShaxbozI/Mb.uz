from .views import CertificateView
from django.urls import path, include
from .views import CertificateCreateView

urlpatterns = [
    path('', CertificateView.as_view(), name='certificate'),
    path('api/create/', CertificateCreateView.as_view(), name='certificate-create'),
]