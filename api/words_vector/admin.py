from django.contrib import admin
from .models import Logs

# Register your models here.


@admin.register(Logs)
class TextAdmin(admin.ModelAdmin):
    list_display = ('files', 'vocabulary', 'vectors')
