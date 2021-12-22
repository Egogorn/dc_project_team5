from django.contrib import admin
from .models import StudentGroup, Task, Profile
# Register your models here.

#admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'group', 'is_teacher')

admin.site.register(Profile, ProfileAdmin)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    pass