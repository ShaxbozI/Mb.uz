from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator

from accounts.tasks import send_email

from .models import TeacherAndStudent, Events, Projects, Gallery, Technology
from .forms import (
    CustomTeacherAndStudentForm, 
    CustomEventsForm, 
    CustomProjectsForm, 
    CustomGalleryForm,
    CustomTeacherSendMailForm, 
    CustomTechnologyForm,
    CustomCoursesForm,
    CustomNumberCertificateForm,
    )
from certificate.models import Courses, NumberCertificate, Certificate, Links
from accounts.models import Contact, CustomUser, SendMail
from accounts.forms import CustomContactForm
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin




class HomeTemplateView(View):
    def get(self, request):
        events = Events.objects.all().order_by('-id')[:1]
        students = TeacherAndStudent.objects.all().filter(status = 'ST').order_by('-id')[:4]
        teachers = TeacherAndStudent.objects.all().filter(status = 'TC')[:10]
        projects = Projects.objects.all().order_by('-id')[:4]
        
        context = {
            'events': events,
            'students': students,
            'teachers': teachers,
            'projects': projects,
            'home_status': 'active'
        }
        return render(request, 'home.html', context)



class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self):
        context = {'about_status': 'active'}
        return context



class ContactView(View):
    def get(self, request):
        contact_form = CustomContactForm()
        context = {'contact_form':contact_form, 'contact_status': 'active'}
        return render(request, 'contact.html', context)
    
    def post(self, request):
        contact_form = CustomContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            contact_form = CustomContactForm()
            messages.success(request, "Xabar yuborildi")
            context = {
                'contact_form':contact_form,
            }
            return render(request, 'contact.html', context)
        else:
            messages.error(request, "Yuborishda xatolik iltimos malumotlarni to'gri kiriting")
            context = {
                'contact_form':contact_form,
            }
            return render(request, 'contact.html', context)



class EventView(View):
    def get(self, request, type):
        events = Events.objects.all()
        now = datetime.now()
        if type == 'all':
            events = Events.objects.all().order_by('-start_data')
        if type == 'gte':
            events = Events.objects.all().filter(start_data__gte=now).order_by('start_data')
        if type == 'lte':
            events = Events.objects.all().filter(start_data__lte=now).order_by('start_data')
        
        search_query = request.GET.get('q')
        if search_query:
            events = events.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
            
        page_events = Paginator(events, 8)
        page_num = request.GET.get('page', 1)
        page_obj = page_events.get_page(page_num)
        
        context = {
            'events': page_obj,
            'event_status': 'active'
        }
        
        return render(request, 'pages/events.html', context)
    
    
    
class GalleryView(View):
    def get(self, request):
        gallery = Gallery.objects.all().order_by('-id')
        
        page_students = Paginator(gallery, 24)
        page_num = request.GET.get('page', 1)
        page_obj = page_students.get_page(page_num)
        
        context = {
            'gallery': page_obj,
            'gallery_status': 'active'
        }
        return render(request, 'pages/gallery.html', context)



class ProjectView(View):
    def get(self, request, types, course):
        technology = Technology.objects.all()
        courses = Courses.objects.all()
        get_course = ''
        if types == 'all':
            projects = Projects.objects.all().order_by('-id')
        elif types == 'techno':
            projects = Projects.objects.all().filter(technologies__technology__icontains=course).order_by('-id')
        else:
            projects = Projects.objects.all().filter(course__name__icontains=course).order_by('-id')
            get_course = course.title()
        
        context = {
            'projects': projects,
            'technology': technology,
            'courses': courses,
            'course': get_course,
            'project_status': 'active'
        }
        return render(request, 'pages/project.html', context)
    
    
    
class StudentView(View):
    def get(self, request, num):
        students = TeacherAndStudent.objects.all().filter(status = 'ST').order_by('-id')
        courses = Courses.objects.all()
        course = ''
        if num == 'all':
            one_student = ''
        elif num.isnumeric():
            one_student = TeacherAndStudent.objects.all().get(id = num)
        else:
            students = students.filter(course__name__icontains = num)
            course = num
            one_student = ''
            
        page_students = Paginator(students, 18)
        page_num = request.GET.get('page', 1)
        page_obj = page_students.get_page(page_num)
        
        context = {
            'students': page_obj,
            'courses': courses,
            'one_student': one_student,
            'course': course,
            'student_status': 'active'
        }
        return render(request, 'pages/students.html', context)
    
    
    
class TeachersView(View):
    def get(self, request):
        teachers = TeacherAndStudent.objects.all().filter(status = 'TC').order_by('-id')
        context = {
            'teachers': teachers,
            'teacher_status': 'active'
        }
        return render(request, 'pages/teachers.html', context)



class AddInfoView(View):
    def get(self, request):
        ts_form = CustomTeacherAndStudentForm()
        event_form = CustomEventsForm()
        project_form = CustomProjectsForm()
        gallery_form = CustomGalleryForm()
        techno_form = CustomTechnologyForm()
        course_form = CustomCoursesForm()
        numcert_form = CustomNumberCertificateForm()
        
        certificate = Certificate.objects.all().order_by('-id')
        links = Links.objects.all()
        application_len = len(certificate)
        
        contat_message = Contact.objects.all().order_by('-id')
        message_len = len(contat_message)
        
        context = {
            'ts_form': ts_form,
            'event_form': event_form,
            'project_form': project_form,
            'gallery_form': gallery_form,
            'techno_form': techno_form,
            'course_form': course_form,
            'numcert_form': numcert_form,
            'certificate': certificate,
            
            'application_len': application_len,
            'links': links,
            
            'contat_message': contat_message,
            'message_len': message_len,
        }
        return render(request, 'addinfo/addinfo.html', context)
    
    def post(self, request, form):
        ts_form = CustomTeacherAndStudentForm()
        event_form = CustomEventsForm()
        project_form = CustomProjectsForm()
        gallery_form = CustomGalleryForm()
        techno_form = CustomTechnologyForm()
        course_form = CustomCoursesForm()
        numcert_form = CustomNumberCertificateForm()
        
        certificate = Certificate.objects.all().order_by('-id')
        links = Links.objects.all()
        application_len = len(certificate)
        
        contat_message = Contact.objects.all().order_by('-id')
        message_len = len(contat_message)
        
        if form == 'TandS':
            ts_form = CustomTeacherAndStudentForm(data=request.POST, files=request.FILES)
            if ts_form.is_valid():
                ts_form.save()
                messages.success(request, 'Malumotlar muvofaqiyatli saqlandi.')
                return redirect(reverse('addinfo'))
            else:
                messages.error(request, "Malumotlarni saqlashda xatolik iltimos malumotlarni to'g'ri kiriting.")
                context = {
                    'ts_form': ts_form,
                    'event_form': event_form,
                    'project_form': project_form,
                    'gallery_form': gallery_form,
                    'techno_form': techno_form,
                    'course_form': course_form,
                    'numcert_form': numcert_form,
                    'certificate': certificate,
                    
                    'application_len': application_len,
                    'links': links,
                    
                    'contat_message': contat_message,
                    'message_len': message_len,
                }
                return render(request, 'addinfo/addinfo.html', context)
                
        if form == 'event':
            event_form = CustomEventsForm(data=request.POST, files=request.FILES)
            if event_form.is_valid():
                event_form.save()
                messages.success(request, 'Malumotlar muvofaqiyatli saqlandi.')
                return redirect(reverse('addinfo'))
            else:
                messages.error(request, "Malumotlarni saqlashda xatolik malumotlarni to'g'ri kiriting. Iltimos sanani '2024-01-01 00:00' ko'rinishda kiriting")
                context = {
                    'ts_form': ts_form,
                    'event_form': event_form,
                    'project_form': project_form,
                    'gallery_form': gallery_form,
                    'techno_form': techno_form,
                    'course_form': course_form,
                    'numcert_form': numcert_form,
                    'certificate': certificate,
                    
                    'application_len': application_len,
                    'links': links,
                    
                    'contat_message': contat_message,
                    'message_len': message_len,
                }
                return render(request, 'addinfo/addinfo.html', context)
            
        if form == 'project':
            project_form = CustomProjectsForm(data=request.POST, files=request.FILES)
            if project_form.is_valid():
                project_form.save()
                messages.success(request, 'Malumotlar muvofaqiyatli saqlandi.')
                return redirect(reverse('addinfo'))
            else:
                messages.error(request, "Malumotlarni saqlashda xatolik malumotlarni to'g'ri kiriting.")
                context = {
                    'ts_form': ts_form,
                    'event_form': event_form,
                    'project_form': project_form,
                    'gallery_form': gallery_form,
                    'techno_form': techno_form,
                    'course_form': course_form,
                    'numcert_form': numcert_form,
                    'certificate': certificate,
                    
                    'application_len': application_len,
                    'links': links,
                    
                    'contat_message': contat_message,
                    'message_len': message_len,
                }
                return render(request, 'addinfo/addinfo.html', context)
            
        if form == 'gallery':
            project_form = CustomGalleryForm(data=request.POST, files=request.FILES)
            if project_form.is_valid():
                project_form.save()
                messages.success(request, 'Malumotlar muvofaqiyatli saqlandi.')
                return redirect(reverse('addinfo'))
            else:
                messages.error(request, "Malumotlarni saqlashda xatolik malumotlarni to'g'ri kiriting. Rasm uchun faqat 'png', 'jpg', 'jpeg', birliklar qabul qilinadi.")
                context = {
                    'ts_form': ts_form,
                    'event_form': event_form,
                    'project_form': project_form,
                    'gallery_form': gallery_form,
                    'techno_form': techno_form,
                    'course_form': course_form,
                    'numcert_form': numcert_form,
                    'certificate': certificate,
                    
                    'application_len': application_len,
                    'links': links,
                    
                    'contat_message': contat_message,
                    'message_len': message_len,
                }
                return render(request, 'addinfo/addinfo.html', context)
            
        if form == 'techno':
            techno_form = CustomTechnologyForm(data=request.POST)
            if techno_form.is_valid():
                techno_form.save()
                messages.success(request, 'Malumotlar muvofaqiyatli saqlandi.')
                return redirect(reverse('addinfo'))
            else:
                messages.error(request, "Malumotlarni saqlashda xatolik malumotlarni to'g'ri kiriting.")
                context = {
                    'ts_form': ts_form,
                    'event_form': event_form,
                    'project_form': project_form,
                    'gallery_form': gallery_form,
                    'techno_form': techno_form,
                    'course_form': course_form,
                    'numcert_form': numcert_form,
                    'certificate': certificate,
                    
                    'application_len': application_len,
                    'links': links,
                    
                    'contat_message': contat_message,
                    'message_len': message_len,
                }
                return render(request, 'addinfo/addinfo.html', context)
        
        if form == 'course':
            course_form = CustomCoursesForm(data=request.POST)
            if course_form.is_valid():
                course_form.save()
                messages.success(request, 'Malumotlar muvofaqiyatli saqlandi.')
                return redirect(reverse('addinfo'))
            else:
                messages.error(request, "Malumotlarni saqlashda xatolik malumotlarni to'g'ri kiriting.")
                context = {
                    'ts_form': ts_form,
                    'event_form': event_form,
                    'project_form': project_form,
                    'gallery_form': gallery_form,
                    'techno_form': techno_form,
                    'course_form': course_form,
                    'numcert_form': numcert_form,
                    'certificate': certificate,
                    
                    'application_len': application_len,
                    'links': links,
                    
                    'contat_message': contat_message,
                    'message_len': message_len,
                }
                return render(request, 'addinfo/addinfo.html', context)
            
        if form == 'num_certficate':
            numcert_form = CustomNumberCertificateForm(data=request.POST)
            if numcert_form.is_valid():
                numcert_form.save()
                messages.success(request, 'Malumotlar muvofaqiyatli saqlandi.')
                return redirect(reverse('addinfo'))
            else:
                messages.error(request, "Malumotlarni saqlashda xatolik malumotlarni to'g'ri kiriting.")
                context = {
                    'ts_form': ts_form,
                    'event_form': event_form,
                    'project_form': project_form,
                    'gallery_form': gallery_form,
                    'techno_form': techno_form,
                    'course_form': course_form,
                    'numcert_form': numcert_form,
                    'certificate': certificate,
                    
                    'application_len': application_len,
                    'links': links,
                    
                    'contat_message': contat_message,
                    'message_len': message_len,
                }
                return render(request, 'addinfo/addinfo.html', context)
                
                

class SendMessageTeacherView(LoginRequiredMixin, View):
    def get(self, request):
        teachers = CustomUser.objects.all().filter(status_teacher = True)
        email_form = CustomTeacherSendMailForm()
        context = {
            'email_form': email_form
        }
        return render(request, 'accounts/send_mail.html', context)
    
    def post(self, request):
        email_form = CustomTeacherSendMailForm(request.POST)
        teachers = CustomUser.objects.all().filter(status_teacher = True)
        if email_form.is_valid():
            title = email_form.cleaned_data.get('title'),
            message = email_form.cleaned_data.get('message'),
            send_mail = SendMail(
                title = title[0],
                message = message[0],
                email = "abdullayevshaxboz1957@gmail.com",
                teacher_email = "example_info@email.com",
                )
            
            send_mail.save()
            
            for teacher in teachers:
                print(teacher.email)
                send_email.delay(
                    title[0],
                    message[0],
                    "abdullayevshaxboz1957@gmail.com",
                    [teacher.email]
                )
            
            
            messages.success(request, "Malumotlar muvofaqiyatli saqlandi va Tez orada xabar barcha o'qituvchilarga yetkaziladi!")
            return redirect(reverse('send_mail'))
        else:
            messages.error(request, "Malumotlarni saqlashda xatolik iltimos malumotlarni to'g'ri kiriting.")
            return render(request, 'accounts/send_mail.html', {'email_form': email_form})
        
        
        
        


def delete_view(request, types, id):
    if types == 'certificate':
        certificate = Certificate.objects.all().filter(id=id)
        certificate.delete()
    if types == 'message':
        contat_message = Contact.objects.all().filter(id=id)
        contat_message.delete()
    return redirect(reverse('addinfo'))
        
    
    
           