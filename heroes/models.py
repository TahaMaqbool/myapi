from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
