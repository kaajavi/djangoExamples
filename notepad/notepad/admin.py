from django.contrib import admin
from notepad.models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('content',)
    list_filter = ('user','date')
    list_display = ('title', 'user', 'date')

admin.site.register(Note, NoteAdmin)