# Generated by Django 5.1.7 on 2025-03-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_rename_level_question_difficulty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='incorrect_answers',
        ),
        migrations.AddField(
            model_name='question',
            name='incorrect_answer',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
