from django.contrib import admin
from .models import Alumni, Teacher, Student, Event, Blog

# Register your models here.


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'graduation_year', 'user_type')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('graduation_year', 'user_type')
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'user_type')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('user_type',)
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'branch')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('branch',)
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'time')
    search_fields = ('title', 'description')
    list_filter = ('date',)
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    raw_id_fields = ('author',)
   