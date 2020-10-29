from django.contrib import admin
from .models import FirstYear, SecondYear, ThirdYear, FourthYear


# Register your models here.

class StudentsDetailsAdmin(admin.ModelAdmin):
    list_display = ('usn', 'name', 'branch', 'section')
    list_display_links = ('usn', 'name', 'branch', 'section')


admin.site.register(FirstYear, StudentsDetailsAdmin)
admin.site.register(SecondYear, StudentsDetailsAdmin)
admin.site.register(ThirdYear, StudentsDetailsAdmin)
admin.site.register(FourthYear, StudentsDetailsAdmin)
