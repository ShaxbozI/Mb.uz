from django.db import models
from certificate.models import Courses
from ckeditor.fields import RichTextField



class Technology(models.Model):
    technology = models.CharField(max_length=150)
    def __str__(self):
        return self.technology



class TeacherAndStudent(models.Model):
    
    class Status(models.TextChoices):
        Student = 'ST', 'Student'
        Teacher = 'TC', 'Teacher'
    
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    info = RichTextField()
    email_link = models.EmailField(max_length=250)
    image = models.ImageField(upload_to='images/tands', default='images/default_picture_tands.png')
    linkedin = models.URLField(blank=True, null=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    # jobs = models.CharField(max_length=350)
    status = models.CharField(
        max_length = 2,
        choices = Status.choices
    )
    cterate_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self): 
        return f'{self.name} {self.last_name}'
    
    def get_full_name(self): 
        return f'{self.name} {self.last_name}'
    
    
class Events(models.Model):
    title = models.CharField(max_length=300)
    # speaker = models.CharField(max_length=150)
    description = RichTextField()
    image = models.ImageField(upload_to='images/events', default='images/default_picture_event.png')
    start_data = models.DateTimeField()
    event_link = models.URLField(blank=True, null=True)
    cterate_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self): 
        return self.title
    
    

class Projects(models.Model):
    title = models.CharField(max_length=300)
    description = RichTextField()
    image = models.ImageField(upload_to='images/projects', default='images/default_picture_project.png')
    project_link = models.URLField(blank=True, null=True)    # kiritishni majburiy qilish kerak
    cterate_at = models.DateTimeField(auto_now_add = True)
    technologies = models.ManyToManyField(Technology)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self): 
        return self.title
    
    
     
class Gallery(models.Model):
    name = models.CharField(max_length=200)
    image_gallery = models.ImageField(upload_to='images/gallery', blank=False)
    
    def __str__(self):
        return self.name