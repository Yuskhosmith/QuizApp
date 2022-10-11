# Generated by Django 4.1.2 on 2022-10-10 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0002_question_answer_quiz_question_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respondance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responder', models.CharField(max_length=20)),
                ('correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizApp.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizApp.quiz')),
            ],
        ),
    ]