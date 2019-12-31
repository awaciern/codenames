from django.contrib import admin
from .models import Word

# Register your models here.
class WordAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')

admin.site.register(Word, WordAdmin)
