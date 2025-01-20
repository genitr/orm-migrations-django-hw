from django.contrib import admin

from .models import Student, Teacher, StudentTeacher


class StudentTeacherInline(admin.TabularInline):
    model = StudentTeacher
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        StudentTeacherInline,
    ]

    list_display = ('id', 'name', 'group')
    list_display_links = ('id', 'name')
    list_filter = ('group',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')
    list_display_links = ('id', 'name')
    list_filter = ('subject',)
