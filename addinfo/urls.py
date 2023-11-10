from django.urls import path
from .views import (
    HomeTemplateView, 
    AddInfoView, 
    AboutView, 
    ContactView, 
    EventView, 
    ProjectView, 
    StudentView, 
    TeachersView, 
    GalleryView, 
    SendMessageTeacherView,
    delete_view
)

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    
    # pages
    path('pages/events/<str:type>/', EventView.as_view(), name='events'),
    # path('pages/projects/', ProjectView.as_view(), name='projects'),
    path('pages/projects/<str:types>/<str:course>/', ProjectView.as_view(), name='projects'),
    path('pages/students/<str:num>/', StudentView.as_view(), name='students'),
    path('pages/students/<int:num>/', StudentView.as_view(), name='students'),
    path('pages/teachers/', TeachersView.as_view(), name='teachers'),
    path('pages/gallery/', GalleryView.as_view(), name='gallery'),
    
    path('page/admin/add/info/', AddInfoView.as_view(), name='addinfo'),
    path('page/admin/add/info/<str:form>/', AddInfoView.as_view(), name='addform'),
    
    path('send/mail/', SendMessageTeacherView.as_view(), name='send_mail'),
    path('delete/<str:types>/<int:id>/', delete_view, name='delete'),
]