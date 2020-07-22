from django.contrib import admin

from .models import *

admin.site.register(Student)
admin.site.register(Classroom)

@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ('students', 'classrooms', 'school_fees', 'received_fees', 'Remaining_fees', 'phone_number', 'completed')
    list_filter = ('completed', 'classrooms', 'publish_date', 'students')
    search_fields = ('completed', 'school_fees', 'students')
    date_hierarchy = 'publish_date'
    ordering = ('completed', 'publish_date', 'school_fees', 'classrooms')
    
admin.site.site_header = 'ADMIN DASHBOARD'
admin.site.site_title = 'STUDENT FEES MANAGEMENT SYSTEM'
admin.site.index_title = 'WELCOME TO STUDENT FESS MANAGEMENT SYSTEM'