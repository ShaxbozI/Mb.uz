from blog.views import BlogView, AddBlogView, BlogDetailView, EditBlogView, delete_blog
from django.urls import path


urlpatterns = [
    path('page/<str:types>/<str:get>/', BlogView.as_view(), name='blogs'),
    path('<str:slug>/', BlogDetailView.as_view(), name='detail_blog'),
    path('page/add', AddBlogView.as_view(), name='add_blogs'),
    path('edit/<int:id>/', EditBlogView.as_view(), name='edit_blog'),
    
    path('delete/<int:id>/', delete_blog, name='delete'),
]