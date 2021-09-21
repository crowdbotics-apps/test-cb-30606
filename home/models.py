from django.conf import settings
from django.db import models


class Home(models.Model):
    "Generated Model"
    name = models.BooleanField()
    desc = models.CharField(
        max_length=256,
    )
