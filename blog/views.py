from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator

from .models import BlogReview, Categories, Tags, Blogs
from .forms import CustomBlogForm, BlogForm, CustomBlogReviewForm

from hitcount.views import HitCountDetailView
from hitcount.views import HitCountMixin
from hitcount.utils import get_hitcount_model



class BlogView(View):
    def get(self, request, types, get):
        categories = Categories.objects.all().order_by('-id')
        tags_all = Tags.objects.all()
        blog = Blogs.objects.all().order_by('-id')
        if types == 'all':
            blogs = Blogs.objects.all().order_by('-id')
            message = ''
        elif types == 'category':
            blogs = Blogs.objects.all().filter(category__name = get).order_by('-id')
            message = f'{get.title()}: hozircha ushbu turkumda bloglar mavjud emas'
        elif types == 'tag':
            blogs = Blogs.objects.filter(tags__name__icontains = get).order_by('-id')
            message = f'#{get}: hozircha ushbu tag ostida bloglar mavjud emas'
        else:
            search_query = request.GET.get('q')
            if search_query:
                blogs = blog.filter(Q(title__icontains=search_query))
                message = ''
            else:
                blogs = []
                message = 'Blog yoki bloglar topilmadi'
        
        
        page_events = Paginator(blogs, 8)
        page_num = request.GET.get('page', 1)
        page_obj = page_events.get_page(page_num)
        
        context = {
            'blogs': page_obj,
            'categories': categories,
            'tags': tags_all,
            'message': message,
            'blog_status': 'active'
        }
        return render(request, 'pages/blog.html', context)


    
    
class BlogDetailView(View):
    def get(self, request, slug):
        blog = Blogs.objects.get(slug = slug)
        categories = Categories.objects.all().order_by('-id')
        tags_all = Tags.objects.all().order_by('-id')
        previous_blog = Blogs.objects.filter(id__lt=blog.id).order_by('-id').first()
        next_blog = Blogs.objects.filter(id__gt=blog.id).order_by('id').first()
        category_blog = Blogs.objects.all().filter(category__name = blog.category).order_by('-id')
        review_form = CustomBlogReviewForm()
        all_review = BlogReview.objects.all().filter(blog__slug = slug)
        len_review = len(all_review)
        
        context = {}
        hit_count = get_hitcount_model().objects.get_for_object(blog)
        hits = hit_count.hits
        hitcontext = context['hitcount'] = {'pk': hit_count.pk}
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        
        
        if hit_count_response.hit_counted:
            hits = hits + 1
            hitcontext['hit_counted'] = hit_count_response.hit_counted
            hitcontext['hit_message'] = hit_count_response.hit_message
            hitcontext['total_hits'] = hits
        
        if all_review:
            rounded_stars = sum(comment.stars_given for comment in all_review)/len(all_review)
            stars_sum = round(rounded_stars, 1)
        else:
            stars_sum = 0
        
        context = {
            'blog': blog,
            'categories': categories,
            'tags': tags_all,
            
            'previous_blog': previous_blog,
            'next_blog': next_blog,
            'category_blog': category_blog,
            
            'review_form': review_form,
            'all_review': all_review,
            'len_review': len_review,
            'stars_sum': stars_sum,
        }
        return render(request, 'pages/blog_detail.html', context )
    
    def post(self, request, slug):
        blog = Blogs.objects.get(slug = slug)
        user = request.user
        review_form = CustomBlogReviewForm(request.POST)
        if review_form.is_valid():
            review = BlogReview(
                blog = blog,
                user = user,
                stars_given = review_form.cleaned_data['stars_given'],
                comment = review_form.cleaned_data['comment']
            )
            review.save()
        return redirect('detail_blog', slug=slug)

    
    
    
class AddBlogView(View):
    def get(self, request):
        blog_form = CustomBlogForm()
        context = {
            'blog_form': blog_form,
        }
        return render(request, 'add_blog.html', context)
    def post(self, request):
        blog_form = CustomBlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            # Ma'lumotlarni olish
            title = blog_form.cleaned_data['title']
            content = blog_form.cleaned_data['content']
            image = blog_form.cleaned_data['image']
            category = blog_form.cleaned_data['category']
            tags = blog_form.cleaned_data['tags']

            # Blogni yaratish
            blog = Blogs(title=title, content=content, image=image, category=category, author=request.user)
            blog.save()
            blog.tags.set(tags)
            blog_slug = Blogs.objects.get(id=blog.id)
            return redirect('detail_blog', slug=blog_slug.slug)
        else:
            context = {
                'blog_form': blog_form,
            }
            return render(request, 'add_blog.html', context)
    
    


class EditBlogView(View):
    def get(self, request, id):
        blog = Blogs.objects.all().get(id=id)
        blog_form = CustomBlogForm(instance=blog)
        context = {
            'blog_form': blog_form,
        }
        return render(request, 'add_blog.html', context)
    def post(self, request, id):
        blog = Blogs.objects.all().get(id=id)
        blog_form = CustomBlogForm(instance=blog, data = request.POST, files = request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('detail_blog', slug=blog.slug)
        else:
            context = {
                'blog_form': blog_form,
            }
            return render(request, 'add_blog.html', context)
    


def delete_blog(request, id):
    blog = Blogs.objects.all().filter(id=id)
    blog.delete()
    return redirect('profile')
    


