from django.contrib import admin
from .models import FourthYearASec


# Register your models here.

class StudentsDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'usn', 'status', 'etime', 'ltime')
    list_display_links = ('name', 'usn', 'status','etime', 'ltime')


admin.site.register(FourthYearASec, StudentsDetailsAdmin)

