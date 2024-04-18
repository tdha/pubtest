from django.db import models
from datetime import date

class Article(models.Model):
    web_url = models.CharField(max_length=255)
    headline = models.TextField()
    trail_text = models.TextField()
    body = models.TextField()
    date = models.DateField(default=date.today)
    summary = models.TextField(blank=True)
    question = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id}: {self.headline}"
    
    class Meta:
        ordering = ['-id']