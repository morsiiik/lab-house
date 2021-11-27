from django import forms
from django.contrib import admin
from django.forms import ModelChoiceField

from .models import *


class LabAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_available', 'deadline')
    list_display_links = ('id', 'title')


class UserLabAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            return ModelChoiceField(User.objects.filter(is_superuser=False))
        if db_field.name == 'mentor':
            return ModelChoiceField(User.objects.filter(is_superuser=True))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Lab, LabAdmin)
admin.site.register(UserLab, UserLabAdmin)
