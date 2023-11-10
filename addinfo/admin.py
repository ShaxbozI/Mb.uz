from django.contrib import admin

from .models import TeacherAndStudent, Events, Projects, Technology


admin.site.register(TeacherAndStudent)
admin.site.register(Events)
admin.site.register(Projects)
admin.site.register(Technology)

