from django import forms
from django.core.mail import send_mail
from .tasks import send_email
from .models import CustomUser, Contact
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class BootstrapStyleMixin:
    field_names = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        
        if self.field_names:
            for fieldname in self.field_names:
                self.fields[fieldname].widget.attrs = {'class': 'form-control mt-1'}
        else:
            raise ValueError('The field_names must be set')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Kalit so'z", widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Kalit so'zni tasdiqlash", widget=forms.PasswordInput)
    class Meta():
        model = CustomUser
        fields = (
            'username',
            'email',
            'certificate_number',
            'course_name',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value for the course_name field to the desired option
        self.fields['course_name'].empty_label = "Kursni tanlang" 
        
    def clean_password_2(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password and password_2 and password != password_2:
            raise forms.ValidationError('Parol kiritishda xatolik iltimos qaytadan kiriting')
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
         
        if user.email:
            send_email.delay(
                "Xush kelibsiz",
                f"Assalomu aleykum {user.username} ro'yhatdan o'tganingiz uchun tashakkur",
                "abdullayevshaxboz1957@gmail.com",
                [user.email]
            )
        
        
        return user
    

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'course_name',
            'profile_picture',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        
        if self.fields:
            for fieldname in self.fields:
                self.fields[fieldname].widget.attrs = {'class': 'form-control mt-1'}
                if fieldname == 'course_name':
                    self.fields[fieldname].empty_label = "Kursni tanlang" 
        else:
            raise ValueError('The field_names must be set')
    
    

class CustomRegisterForm(BootstrapStyleMixin, RegisterForm):
    field_names = [  'username', 'email', 'certificate_number', 'password', 'password_2',]


class CustomLoginForm(BootstrapStyleMixin, LoginForm):
    field_names = ['username', 'password', ]  
    

class CustomResetPasswordForm(BootstrapStyleMixin, PasswordResetForm):
    field_names = ['email', ]
    
    
class CustomSetPassForm(BootstrapStyleMixin, SetPasswordForm):
    new_password1 = forms.CharField(label="Yangi kalit so'z", widget=forms.PasswordInput,)
    new_password2 = forms.CharField(label="Kalit so'zni tasdiqlash", widget=forms.PasswordInput)
    field_names = ['new_password1', 'new_password2', ]
    
    
    
    



#    CONTACT

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = (
            'name',
            'email',
            'title',
            'message',
        )
        
    def save(self, commit=True):
        message = super().save(commit)
        message.save()
         
        if message.email:
            send_email.delay(
                "Mohirbitiruvchi qayta_aloqa",
                f"Assalomu aleykum {message.name} siz Mohirbitiruvchiga xabar yo'ladingiz. Biz uni tez orada ko'rib chiqamiz va sizga bu haqida xabar qilamiz. Hurmat bilan https://MohirBitiruvchi.uz jamoasi",
                "abdullayevshaxboz1957@gmail.com",
                [message.email]
                
            )
        return message
        

class CustomContactForm(BootstrapStyleMixin, ContactForm):
    field_names = (
            'name',
            'email',
            'title',
            'message',
        )
