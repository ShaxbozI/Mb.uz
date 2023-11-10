from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views import View
from .models import CustomUser

from blog.models import Blogs
from certificate.models import NumberCertificate

from .forms import CustomRegisterForm, CustomLoginForm, CustomResetPasswordForm, CustomSetPassForm, ProfileEditForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

from .tasks import send_email





class AuthView(View):
    def get(self, request):
        login_form = CustomLoginForm()
        register_form = CustomRegisterForm()
        context = {
            'login_form': login_form,
            'register_form': register_form,
        }
        return render(request, 'accounts/login_register.html', context)
    
    
    def post(self, request, form):

        if form == 'login':
            login_form = CustomLoginForm(data=request.POST)
            register_form = CustomRegisterForm(data=request.POST)
            if login_form.is_valid():
                data = login_form.cleaned_data
                user = authenticate(request, username=data['username'], password=data['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(reverse('home'))
                    else:
                        messages.error(request, "Foydalanuvchi aktiv emas")
                else:
                    messages.error(request, "Foydalanuvchi nomi yoki maxfiy so'z xato!")
                    context = {
                        'login_form': login_form,
                        'register_form': register_form,
                    }
                    return render(request, 'accounts/login_register.html', context)
            else:
                context = {
                    'login_form': login_form,
                    'register_form': register_form,
                }
                return render(request, 'accounts/login_register.html', context)
        
        elif form == 'register':
            login_form = CustomLoginForm(request.POST)
            register_form = CustomRegisterForm(request.POST)
            if register_form.is_valid():
                certificate = register_form.cleaned_data.get('certificate_number')
                email = register_form.cleaned_data.get('email')
                
                context = {
                    'login_form': login_form,
                    'register_form': register_form,
                    'class': 'auto-press'
                }
                #  Sertificat raqamini tekshirish
                if certificate:
                    # Bazadagi sertifikat raqamlariga tekshirish
                    certificate_number = NumberCertificate.objects.all().filter(number=certificate).exclude()
                    if certificate_number:
                        user_certificate = CustomUser.objects.filter(certificate_number=certificate)
                        # raqam bazada ham mavjud bo'lsa ushbu raqam biror foydalanuvchiga tegishli emasligini tekshirish
                        if not user_certificate:
                            # certifikat tekshiruvdan o'tdi
                            # endi emailni tekshiramiz kiritilgan emaildan biror foydalanuvchi faoydalanmayotgan bo'lishi kerak
                            if email:
                                # biror foydalanuvchi faoydalanmayotganni tekshirish
                                user_email = CustomUser.objects.filter(email=email).first()
                                if user_email:
                                    print(user_email.status_teacher)
                                    if user_email.status_teacher:
                                        messages.success(request, f"Assalomu aleykum ustoz {user_email.username} siz allaqachon admin tomonidan ro'yhatdan o'tkazilgansiz. Maxfiy so'zni qayta tiklash sahifasiga o'tib maxfiy so'z o'rnatishingiz mumkin!")
                                        return redirect(reverse('authenticated'))
                                    else:
                                        messages.error(request, "Siz kiritgan Email allaqachon faydalanilmoqda!")
                                        return render(request, 'accounts/login_register.html', context)
                                else:
                                    # certificat va email tekshiruvdan o'tsa userni saqlash
                                    register_form.save()
                                    return redirect(reverse('authenticated'))
                        else:
                            messages.error(request, "Siz kiritgan sertifikat raqami boshqa Bitiruvchiga tegshli!")
                            return render(request, 'accounts/login_register.html', context)
                    else:
                        messages.error(request, "Noto'g'ri sertifikat raqmini kiritdingiz iltimos tekshirib qaytadan kiriting!")
                        return render(request, 'accounts/login_register.html', context)
                    
                # emailni tekshirish
                elif email:
                    user_email = CustomUser.objects.filter(email=email).first()
                    if user_email:
                        if user_email.status_teacher:
                            messages.success(request, f"Assalomu aleykum ustoz {user_email.username} siz allaqachon admin tomonidan ro'yhatdan o'tkazilgansiz. Maxfiy so'zni qayta tiklash sahifasiga o'tib maxfiy so'z o'rnatishingiz mumkin!")
                            return redirect(reverse('authenticated'))
                        else:
                            messages.error(request, "Siz kiritgan Email allaqachon faydalanilmoqda!")
                            return render(request, 'accounts/login_register.html', context)
                        
                    else:
                        register_form.save()
                        return redirect(reverse('authenticated'))
                    
            else:
                context = {
                    'login_form': login_form,
                    'register_form': register_form,
                    'class': 'auto-press'
                }
                messages.error(request, "Bunday nomdagi foydalanuvchi mavjud!")
                return render(request, 'accounts/login_register.html', context)
            
            
 

class ProfileEdit(View):
    pass


 
 
class ProfileView(View):
    def get(self, request):
        form_update = ProfileEditForm(instance=request.user)
        author_blog = Blogs.objects.filter(author = request.user.id).order_by('-id')
        context = {
            'form': form_update, 
            'blogs': author_blog
            }
        return render(request, 'accounts/profile_info.html', context)
    
    def post(self, request):
        form_update = ProfileEditForm(instance = request.user, data = request.POST, files=request.FILES)
        if form_update.is_valid():
            form_update.save()
            phone_number = form_update.cleaned_data.get('phone_number')
            return redirect('profile')
        else:
            messages.error(request, "Iltimos maxfiy so'zni qayta kiriting.")
            message = "Yandilangan Malumotlar tasdiqlanmadi Iltimos diqqat bilan to'ldiring!"
            class_name = 'active'
            phone_number = form_update.cleaned_data.get('phone_number')
            
        print(phone_number)
        context = {
            'form': form_update,  
            'class_name': class_name,
            'message': message,
            }
        return render(request, 'accounts/profile_info.html', context )
 
 
 
 
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
 
 
 
            
# class CustomPasswordResetView(PasswordResetView):
#     template_name = 'accounts/reset_password/password_reset.html'
#     form_class = CustomResetPasswordForm
#     success_url = reverse_lazy('forgot_password')
#     email_template_name = 'accounts/reset_password/password_reset_email.html'
    
#     def post(self, request):
#         form_class = CustomResetPasswordForm(data=request.POST)
#         if form_class.is_valid():
#             email = form_class.cleaned_data['email']
#             user_exists = CustomUser.objects.filter(email=email).exists()
#             if user_exists:
#                 response = super().post(request)
#                 messages.success(request, "Parol tiklash uchun bog'lama email manzilingizga yuborildi.")
#                 return response
#             else:
#                 messages.error(request, "Bunday email manzili topilmadi. Iltimos, ro'yhatdan o'tishda ishlatilgan email manzilini kiriting.")
#         return self.form_invalid(form_class)



from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

class CustomPasswordResetView(View):
    def get(self, request):
        email_form = CustomResetPasswordForm()
        return render(request, 'accounts/reset_password/password_reset.html', {'email_form': email_form})
    def post(self, request):
        email_form = CustomResetPasswordForm(data=request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            user_exists = CustomUser.objects.filter(email=email)
            if user_exists.exists():
                for user in user_exists:
                    subject = "Maxfiy so'zni tiklash"
                    email_template_name = 'accounts/reset_password/password_reset_email.html'
                    parametrs = {
                        'email': user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Mohirbitiruvchi',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        'user': user
                    }
                    email = render_to_string(email_template_name, parametrs)
                    try:
                        send_email.delay(
                            subject,
                            email,
                            'abdullayevshaxboz1957@gmail.com',
                            [user.email],
                        )
                    except:
                        return HttpResponse('Xatolik')
                    messages.success(request, "Parol tiklash uchun bog'lama email manzilingizga yuborildi.")
                    return redirect(reverse('forgot_password'))
            else:
                messages.error(request, "Bunday email manzili topilmadi. Iltimos, ro'yhatdan o'tishda ishlatilgan email manzilini kiriting.")
            return redirect(reverse('forgot_password'))



class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name= 'accounts/reset_password/password_reset_confirm.html'
    form_class = CustomSetPassForm
    success_url = reverse_lazy('authenticated')