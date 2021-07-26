from django.db import models


class HelpdeskModel(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.title
