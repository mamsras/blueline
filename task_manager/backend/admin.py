from django.contrib import admin
from backend.models import Task, User

# Register your models here.
admin.site.register(User)
admin.site.register(Task)