from django.db import models
import datetime


class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    author = models.CharField(max_length=30)
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title
