from django.contrib import admin
from .models import Document, Vocabulary

# Register your models here.


@admin.register(Document)
class TextAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('get_documents', 'vocabulary', 'get_count')

    def get_documents(self, obj):
        return "\n".join([d.name for d in obj.documents.all()])

    def get_count(self, obj):
        return len(obj.vocabulary)

    get_documents.short_description = 'Documents'
    get_count.short_description = 'Words count'
