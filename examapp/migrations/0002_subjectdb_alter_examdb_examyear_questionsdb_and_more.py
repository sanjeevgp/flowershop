# Generated by Django 4.0 on 2022-03-14 08:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subjectdb',
            fields=[
                ('SubjectId', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='SubjectId')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('IsActive', models.BooleanField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='examdb',
            name='ExamYear',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(1900)], verbose_name='Exam Year'),
        ),
        migrations.CreateModel(
            name='questionsdb',
            fields=[
                ('QuestionId', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='QnId')),
                ('QuestionType', models.CharField(max_length=50, verbose_name='Question Type')),
                ('Questions', models.CharField(max_length=250, verbose_name='Questions')),
                ('IsActive', models.BooleanField(default=1)),
                ('Subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='examapp.subjectdb')),
            ],
        ),
        migrations.CreateModel(
            name='optionsdb',
            fields=[
                ('OptionsId', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='OptionsId')),
                ('Options', models.CharField(max_length=100, verbose_name='Options')),
                ('IsActive', models.BooleanField(default=1)),
                ('QuestionId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examapp.questionsdb')),
            ],
        ),
        migrations.CreateModel(
            name='examquestiondb',
            fields=[
                ('ExamquestionId', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='examQuestion')),
                ('IsActive', models.BooleanField(default=1)),
                ('Exam', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examapp.examdb')),
                ('Questions', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examapp.questionsdb')),
            ],
        ),
        migrations.CreateModel(
            name='answeresdb',
            fields=[
                ('AnswerId', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='AnswerID')),
                ('IsActive', models.BooleanField(default=1)),
                ('OptionsId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examapp.optionsdb')),
                ('QuestionId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examapp.questionsdb')),
            ],
        ),
    ]