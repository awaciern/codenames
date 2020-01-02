from django.contrib import admin
from .models import *

# Register your models here.
class WordAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')

admin.site.register(Word, WordAdmin)

admin.site.register(Board)

admin.site.register(Board.BoardWord)
