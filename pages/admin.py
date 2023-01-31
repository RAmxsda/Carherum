from django.contrib import admin
from .models import*
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="50"  style="border-radius: 30px;" />'.format(object.photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('id','thumbnail','first_name','designation')
    list_display_links = ('first_name',)

admin.site.register(Team, TeamAdmin)