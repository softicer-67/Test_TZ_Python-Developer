from django.contrib import admin
from app.models import EducationModule


@admin.register(EducationModule)
class EducationModuleAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'description']
    search_fields = ['number', 'name']
