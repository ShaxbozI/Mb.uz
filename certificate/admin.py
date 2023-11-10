from django.contrib import admin
from .models import Courses, NumberCertificate, Links, Certificate


admin.site.register(Courses)
admin.site.register(NumberCertificate)
admin.site.register(Links)
admin.site.register(Certificate)