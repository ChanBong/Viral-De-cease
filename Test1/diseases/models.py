from django.db import models
from django.contrib.auth.models import User


class Diseas(models.Model):
    name = models.CharField(max_length=100)
    about_s = models.TextField()
    site = models.URLField()

    def __str__(self):
        return self.name
