"""
URL configuration for mohirbitiruvchi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
# from certificate.views import CertificateCreateView


from django.views.generic import RedirectView
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('site/mohirdev/mohirbitiruvchi/admin', admin.site.urls),
    # path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('blogs/', include('blog.urls')),
    path('', include('addinfo.urls')),
    path('certificate/', include('certificate.urls')),
    # path('api/create/', CertificateCreateView.as_view(), name='certificate-create'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.png')),
]

handler404 = "mohirbitiruvchi.views.page_not_found_view"
handler500 = "mohirbitiruvchi.views.server_error_view"

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Override Admin site panel
admin.site.index_title = "Mohirdev"
admin.site.site_header = "Mohirbitiruvchi.uz Admin"
admin.site.site_title = "Mohirbitiruvchi"