from django.db import models
from custom_fields import ListField


class Document(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Vocabulary(models.Model):
    documents = models.ManyToManyField(
        Document, through='DocumentVocabulary', blank=True
    )
    vocabulary = ListField(blank=True, null=True)

    def __str__(self):
        return str(self.vocabulary)


class DocumentVocabulary(models.Model):
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, db_column='document_id'
    )
    vocabulary = models.ForeignKey(
        Vocabulary, on_delete=models.CASCADE, db_column='vocabulary_id'
    )
