from django.contrib import admin
from .models import CameraNumbers
# Register your models here.

admin.site.site_header = "Attendance Management"


class CameraNumbersAdmin(admin.ModelAdmin):
    list_display = ('Classroom', 'Cameras', 'semester', 'branch', 'year', 'section')
    list_display_links = ('Classroom', 'Cameras', 'semester', 'branch', 'year', 'section')


admin.site.register(CameraNumbers, CameraNumbersAdmin)