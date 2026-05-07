# Register your models here.

from django.contrib import admin
from .models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('username', 'score', 'created_at')
    ordering = ('-score',)
    list_filter = ('created_at',)
    search_fields = ('username',)

admin.site.register(Score, ScoreAdmin)


