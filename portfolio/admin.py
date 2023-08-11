from django.contrib import admin
from .models import ContactMessage, Cv, Category, Project

# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(Cv)
admin.site.register(Category)
admin.site.register(Project)