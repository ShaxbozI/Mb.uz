from django.db import models
from django.forms import ValidationError


class Courses(models.Model):
    name = models.CharField(max_length = 200) 
    def __str__(self):
        return self.name


class Certificate(models.Model):
    def validate_integer(value): 
        try:
            int(value)
        except ValueError:
            raise ValidationError("Faqat son kiriting")
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    course_name = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(max_length=80)
    phone_number = models.CharField(max_length=13, validators=[validate_integer])
    def __str__(self):
        return self.name
    def get_full_name(self):
        return f'{self.name} {self.last_name}' 
    
    
    
class Links(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    link_name = models.CharField(max_length=300)
    link = models.URLField()
    def __str__(self):
        return f'Certificate ID-{self.certificate.id}: {self.certificate.get_full_name()} || link-name:: ({self.link_name})'



class NumberCertificate(models.Model):
    number = models.CharField(max_length=20)
    def __str__(self):
        return self.number 