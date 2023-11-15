from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from accounts.models import CustomUser
from ckeditor.fields import RichTextField



class Categories(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    

class Tags(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

 

class Blogs(models.Model):
        
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    about_title = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='images/blogs', default='images/default_picture_project.png')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    
        

@receiver(pre_save, sender=Blogs)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        
        
        


class BlogReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    stars_given = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.blog.title} : {self.user.username} || {self.stars_given}"