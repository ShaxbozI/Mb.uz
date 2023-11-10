from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
from certificate.models import Courses
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    def validate_integer(value):
        try:
            int(value)
        except ValueError:
            raise ValidationError("Faqat son kiriting")
    profile_picture = models.ImageField(upload_to='images/users', default='images/default_picture_tands.png')
    phone_number = models.CharField(max_length=13, default=123456789123, validators=[validate_integer])
    certificate_number = models.CharField(max_length=20, blank=True, null=True)
    status_student = models.BooleanField(default=False)
    status_teacher = models.BooleanField(default=False)
    course_name = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True, blank=True)
    cterate_at = models.DateTimeField(auto_now_add = True)
    
    
@receiver(pre_save, sender=CustomUser)
def set_audio_file(sender, instance, **kwargs):
    if instance.certificate_number:
        instance.status_student = True
    else:
        instance.status_student = False
        
        
        

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    title = models.CharField(max_length=350)
    message = models.TextField()
    def __str__(self):
        return self.name
    
    
    

class SendMail(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    email = models.EmailField()
    teacher_email = models.EmailField()
    
    def __str__(self):
        return self.title