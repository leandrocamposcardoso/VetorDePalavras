from django.urls import include, path
from django.contrib import admin
from django.conf import settings

api_base = settings.URL_BASE

urlpatterns = [
    path(f"{api_base}admin/", admin.site.urls),
    path(f'{api_base}words_vector/', include('words_vector.urls')),
]
