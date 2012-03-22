from mapstory.models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class SectionAdmin(admin.ModelAdmin):
    list_display = 'id','name','order'
    list_display_links = 'id',
    list_editable = 'name','order'

class VideoLinkAdmin(admin.ModelAdmin):
    list_display = 'id','name','title','href','publish'
    list_display_links = 'id',
    list_editable = 'name','title','publish'

admin.site.register(VideoLink, VideoLinkAdmin)
admin.site.register(Section, SectionAdmin)