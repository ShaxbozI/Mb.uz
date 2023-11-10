from celery import Celery
from mohirbitiruvchi.celery import app
from django.core.mail import send_mail

@app.task()
def send_email(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    
    
    

