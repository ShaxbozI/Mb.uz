from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .forms import CertificateForm, LinksFormSet, CustomCertificateForm
from rest_framework import generics
from .models import Certificate
from .serializers import CertificateSerializer
from django.contrib import messages

# views.py
from rest_framework.response import Response
from .models import Certificate, Links
from rest_framework.permissions import AllowAny
from .serializers import CertificateSerializer, LinksSerializer

class CertificateCreateView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Links.objects.all()
    serializer_class = CertificateSerializer

    def perform_create(self, serializer):
        certificate = serializer.save()

        # Ma'lumotlarni olish
        links_data = self.request.data.get('links')

        # Links obyektlarini yaratish
        for link_data in links_data:
            Links.objects.create(certificate=certificate, **link_data)

        return certificate



class CertificateView(View):
    def get(self, request):
        certificate_form = CustomCertificateForm()
        links_formset = LinksFormSet(queryset=Links.objects.none())
        context = {
            'form': certificate_form,
            'links_formset': links_formset,
            'certificate_status': 'active'
        }
        return render(request, 'certificate.html', context)

    def post(self, request):
        certificate_form = CustomCertificateForm(request.POST)
        links_formset = LinksFormSet(request.POST, queryset=Links.objects.none())

        if certificate_form.is_valid() and links_formset.is_valid():
        # Check if at least one link has been provided
            at_least_one_link_provided = any(link_form.cleaned_data for link_form in links_formset)
        else:
            at_least_one_link_provided = False
        
        if at_least_one_link_provided:
            certificate = certificate_form.save()

            for link_form in links_formset:
                if link_form.cleaned_data:
                    link = link_form.save(commit=False)
                    link.certificate = certificate
                    link.save()
            
            # Clear the forms to prepare for the next entry
            certificate_form = CustomCertificateForm()
            links_formset = LinksFormSet(queryset=Links.objects.none())
            messages.success(request, 'Malumotlar muvofaqiyatli saqlandi.')
            return redirect(reverse('certificate'))
        else:      
            context = {
                'form': certificate_form,
                'links_formset': links_formset,
                'certificate_status': 'active'
            }
            messages.error(request, "Kamida bitta link kiritish shart.")
            return render(request, 'certificate.html', context)