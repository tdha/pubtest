from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone

def validate_current_or_past_year(value):
    current_year = timezone.now().year
    if not (1900 <= value <= current_year):
        raise ValidationError(f"Please enter a year between 1900 and {current_year}")
        
def validate_postcode_range(value):
    if not (200 <= int(value) <= 9944):
        raise ValidationError("Postcode must be between 0200 and 9944.")

postcode_validator = RegexValidator(
    regex=r'^\d{4}$',
    message="Postcode must be a four-digit number."
)

GENDER_CHOICES = (
    ('W', "Would rather not say"),
    ('F', "Female or woman"),
    ('M', "Male or man"),
    ('X', "Non-binary"),
    ('O', "Other"),
)


class Article(models.Model):
    web_url = models.CharField(max_length=255, unique=True)
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


class Response(models.Model):
    answer = models.CharField(max_length=16, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.article.id} - {self.user.username}: {self.answer}"


class Profile(models.Model):
    birth_year = models.IntegerField(
        validators=[validate_current_or_past_year], 
        blank=True,
        null=True
    )
    postcode = models.CharField(
        max_length=4,
        validators=[postcode_validator, validate_postcode_range],
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
