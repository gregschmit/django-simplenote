from django.contrib import admin
from . import models


class NoteAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = list_display


admin.site.register(models.Note, NoteAdmin)
