from rest_framework import serializers
from .models import Document, Vocabulary, DocumentVocabulary
from .nlp import NLP


class DocumentSerializer(serializers.ModelSerializer):
    text = serializers.CharField()

    class Meta:
        model = Document
        fields = ['name', 'text']


class VocabularySerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True)

    def create(self, validated_data):
        nlp = NLP()
        tokens = []
        documents = validated_data.pop('documents', None) or []
        instance = super().create(validated_data)
        for document in documents:
            doc_instance = Document.objects.create(
                text=document['text'], name=document['name']
            )
            DocumentVocabulary.objects.create(
                document=doc_instance, vocabulary=instance
            )
            tokens.extend(nlp.tokenize(document['text']))
        instance.vocabulary = nlp.remove_stopwords(set(tokens))
        instance.save()
        return instance

    class Meta:
        model = Vocabulary
        fields = ['documents', 'vocabulary']
