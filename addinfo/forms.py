from django import forms
from .models import TeacherAndStudent, Events, Projects, Gallery, Technology
from certificate.models import Courses, NumberCertificate
from accounts.models import SendMail




class BootstrapStyleMixin:
    field_names = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.field_names:
            for fieldname in self.field_names:
                self.fields[fieldname].widget.attrs = {'class': 'form-control mt-1'}
        else:
            raise ValueError('The field_names must be set')
        
        
        
class TeacherAndStudentForm(forms.ModelForm):
    class Meta:
        model = TeacherAndStudent
        fields = "__all__"
    

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
    
    
class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = "__all__"
        
        
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"
        

class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = "__all__"


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"
        
        
class NumberCertificateForm(forms.ModelForm):
    class Meta:
        model = NumberCertificate
        fields = "__all__"
        
        
        # subject, message, from_email, recipient_list
    
class TeacherSendMailForm(forms.ModelForm):
    class Meta:
        model = SendMail
        fields = ('title', 'message')
    

class CustomTeacherSendMailForm(BootstrapStyleMixin, TeacherSendMailForm):
    field_names = ('title', 'message')
        
        
        
        
    
    
class CustomTeacherAndStudentForm(BootstrapStyleMixin, TeacherAndStudentForm):
    field_names = ['name', 'last_name', 'info', 'image', 'email_link', 'linkedin', 'course', 'jobs', 'status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.field_names:
            for fieldname in self.field_names:
                if fieldname == 'status':
                    self.fields[fieldname].empty_label = "Statusni tanlang"
        else:
            raise ValueError('The field_names must be set')
    
    
class CustomEventsForm(BootstrapStyleMixin, EventsForm):
    field_names = ['title', 'speaker', 'description', 'image', 'start_data', 'event_link']
    
    
class CustomProjectsForm(BootstrapStyleMixin, ProjectsForm):
    field_names = ['title', 'description', 'image', 'project_link', 'technologies', 'course']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.field_names:
            for fieldname in self.field_names:
                if fieldname == 'course':
                    self.fields[fieldname].empty_label = "Kursni tanlang"
        else:
            raise ValueError('The field_names must be set')
    
    
class CustomGalleryForm(BootstrapStyleMixin, GalleryForm):
    field_names = ['name', 'image_gallery']
    
    
class CustomTechnologyForm(BootstrapStyleMixin, TechnologyForm):
    field_names = ['technology']
    
    
class CustomCoursesForm(BootstrapStyleMixin, CoursesForm):
    field_names = ['name']
    
    
class CustomNumberCertificateForm(BootstrapStyleMixin, NumberCertificateForm):
    field_names = ['number']