from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event, Comment


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    """
    In admin site, lists fields for display of events, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_on', 'category')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


# Register your models here.

admin.site.register(Comment)
