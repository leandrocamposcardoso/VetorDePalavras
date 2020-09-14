from django.db import models
from custom_fields import ListField


class Logs(models.Model):
    files = ListField()
    vocabulary = ListField(null=True, blank=True)
    vectors = ListField(null=True, blank=True)
