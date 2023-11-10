from django import forms
from .models import Certificate, Links
from rest_framework import serializers



class BootstrapStyleMixin:
    field_names = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.field_names:
            for fieldname in self.field_names:
                self.fields[fieldname].widget.attrs = {'class': 'form-control mt-1'}
        else:
            raise ValueError('The field_names must be set')



class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ('name', 'last_name', 'course_name', 'email', 'phone_number')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value for the course_name field to the desired option
        self.fields['course_name'].empty_label = "Kursni tanlang" 

class CustomCertificateForm(BootstrapStyleMixin, CertificateForm):
    field_names = ('name', 'last_name', 'course_name', 'email', 'phone_number')



class LinksForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ('link_name', 'link')
        widgets = {
            'link_name': forms.TextInput(attrs={'class': 'form-control mt-1'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-1 ps-3'}),
        }
    
    
LinksFormSet = forms.modelformset_factory(
    Links, form=LinksForm, extra=10, max_num = 10
)
