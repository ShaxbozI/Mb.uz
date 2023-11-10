from django.contrib import admin
from .models import Categories, Tags, Blogs, BlogReview


admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Blogs)
admin.site.register(BlogReview)