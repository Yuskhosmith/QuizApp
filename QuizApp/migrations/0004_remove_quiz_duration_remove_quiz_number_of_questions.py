# Generated by Django 4.1.2 on 2022-10-10 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0003_respondance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='number_of_questions',
        ),
    ]
