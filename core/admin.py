from django.contrib import admin
from .models import StudentGroup, Task, Profile, Solution
# Register your models here.

#admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'is_teacher')

admin.site.register(Profile, ProfileAdmin)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'deadline')
    pass

@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('task', 'student', 'time')
    pass