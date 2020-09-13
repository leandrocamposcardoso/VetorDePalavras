from rest_framework.viewsets import ModelViewSet
from .models import Vocabulary
from .serializers import VocabularySerializer


class VocabularyView(ModelViewSet):
    serializer_class = VocabularySerializer
    queryset = Vocabulary.objects.all()
