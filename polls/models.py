from django.db import models
from datetime import date

# ANSWERS = (
#     ('U', 'Undecided'),
#     ('Y', 'Yes'),
#     ('N', 'No'),
# )

class Article(models.Model):
    web_url = models.CharField(max_length=255)
    headline = models.TextField()
    trail_text = models.TextField()
    body = models.TextField()
    date = models.DateField(default=date.today)
    summary = models.TextField()
    question = models.TextField()
    # answers = models.CharField(
    #     max_length=1,
    #     choices=ANSWERS,
    #     default=ANSWERS[0][0]
    # )

    def __str__(self):
        return f"{self.id}: {self.headline}"