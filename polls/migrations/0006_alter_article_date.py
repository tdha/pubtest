# Generated by Django 5.0.4 on 2024-04-19 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_article_date_profile_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
