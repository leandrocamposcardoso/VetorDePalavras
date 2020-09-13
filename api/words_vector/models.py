from django.db import models
from custom_fields import ListField


class Logs(models.Model):
    files = ListField()
    vocabulary = ListField()
    vectors = ListField()
