from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


from . import views


router = routers.SimpleRouter(trailing_slash=False)
router.register('vocabulary', views.VocabularyView, basename='vocabulary')

urlpatterns = router.urls + []

urlpatterns = format_suffix_patterns(urlpatterns)
""
