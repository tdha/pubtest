# Generated by Django 5.0.4 on 2024-04-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_article_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='question',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]