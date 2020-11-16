from django.contrib import admin
from .models import Post,Profile

# Register your models here.
# @admin.register(Student)
# class AdminStudent(admin.ModelAdmin):
#     list_display=['id','name','roll_no','description']

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['id', 'titles', 'desc']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'pro_pic','bio','dob','prof','qualif']
