from django.db import models
from django.contrib.auth.models import User


class Diseas(models.Model):
    name = models.CharField(max_length=100)
    about_s = models.TextField()
    site = models.URLField()
    symptoms = models.TextField()
    about_l = models.TextField(blank=True)

    def __str__(self):
        return self.name
