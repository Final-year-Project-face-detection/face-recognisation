from django.contrib import admin
from .models import CameraNumbers, StudentsDetails
# Register your models here.

admin.site.site_header = "Attendance Management"


class CameraNumbersAdmin(admin.ModelAdmin):
    list_display = ('Classroom', 'Cameras', 'semester', 'branch', 'year', 'section')
    list_display_links = ('Classroom', 'Cameras', 'semester', 'branch', 'year', 'section')

class StudentdetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'branch', 'year', 'section')
    list_display_links = ('name', 'semester', 'branch', 'year', 'section')

    
admin.site.register(CameraNumbers, CameraNumbersAdmin)
admin.site.register(StudentsDetails,StudentdetailsAdmin)