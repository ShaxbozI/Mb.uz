from django import forms
from .models import BlogReview, Categories, Tags, Blogs



class BootstrapStyleMixin:
    field_names = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.field_names:
            for fieldname in self.field_names:
                if fieldname != 'tags':
                    self.fields[fieldname].widget.attrs = {'class': 'form-control mt-1'}
                if fieldname == 'tags':
                    self.fields[fieldname].widget.attrs = {'class': 'mt-1 tags-select'}
                if fieldname == 'category':
                    self.fields[fieldname].empty_label = "Turkumni tanlang"
        else:
            raise ValueError('The field_names must be set')
        
        

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title', 'content', 'image', 'category', 'tags')
        
        
class CustomBlogForm(BootstrapStyleMixin, BlogForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    field_names = ['title', 'content', 'image', 'category', 'tags']
    
    
    
    
class BlogReviewForm(forms.ModelForm):
    class Meta:
        model = BlogReview
        fields = ('comment', 'stars_given')
      
class CustomBlogReviewForm(BootstrapStyleMixin, BlogReviewForm):
    field_names = ('comment', 'stars_given')