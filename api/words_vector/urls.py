from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from . import views


router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = router.urls + [
    path('file-vocabulary', views.FileVocabularyView.as_view()),
    path('file-vectors', views.FileVectorView.as_view()),
    path('file-two-grams-vocabulary', views.FileTwoGramsVocabularyView.as_view()),
    path('file-two-grams-vector', views.FileTwoGramsVectorView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
