from enum import auto
from operator import mod
from pickle import TRUE
from pyexpat import model
from ssl import Options
from django.db import models
from django.db.models.base import Model
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class examdb(models.Model):
    ExamId=models.IntegerField(primary_key=True,auto_created=True,verbose_name="Id")
    ExamName=models.CharField(verbose_name="Exam Name",max_length=20)
    ExamType=models.CharField(verbose_name="Exam Type",max_length=25)
    ExamYear=models.IntegerField(verbose_name="Exam Year",blank=True,null=True,validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    ExamDuration=models.CharField(verbose_name="Exam Duration",max_length=20)
    ExamDate=models.DateField(verbose_name="Exam Date")
    IsActive=models.BooleanField(default=1)
    def __str__(self):
        return self.ExamName

class subjectdb(models.Model):
    SubjectId=models.IntegerField(primary_key=True,auto_created=True,verbose_name="SubjectId")
    subject=models.CharField(verbose_name="Subject",max_length=50,unique=TRUE)
    IsActive=models.BooleanField(default=1)
    def __str__(self):
        return self.subject

class questionsdb(models.Model):
    QuestionId=models.IntegerField(primary_key=True,auto_created=True,verbose_name="QnId")
    QuestionType=models.CharField(verbose_name="Question Type",max_length=50)
    Subject=models.ForeignKey(subjectdb,on_delete=models.PROTECT,null=True,blank=True)
    Questions=models.CharField(verbose_name="Questions",max_length=250)
    IsActive=models.BooleanField(default=1)
    def __str__(self):
        return self.Questions

class optionsdb(models.Model):
    OptionsId=models.IntegerField(primary_key=True,auto_created=True, verbose_name="OptionsId")
    Options=models.CharField(verbose_name="Options",max_length=100)
    QuestionId=models.ForeignKey(questionsdb,on_delete=models.PROTECT)
    IsActive=models.BooleanField(default=1)
    def _str_(self):
        return self.Options

class answeresdb(models.Model):
    AnswerId=models.IntegerField(primary_key=True,verbose_name="AnswerID",auto_created=True)
    QuestionId=models.ForeignKey(questionsdb,on_delete=models.PROTECT)
    OptionsId=models.ForeignKey(optionsdb,on_delete=models.PROTECT)
    IsActive=models.BooleanField(default=1)
    def __str__(self):
        return str(self.AnswerId)

class examquestiondb(models.Model):
    ExamquestionId=models.IntegerField(primary_key=True,auto_created=True,verbose_name="examQuestion")
    Exam=models.ForeignKey(examdb,on_delete=models.PROTECT)
    Questions=models.ForeignKey(questionsdb,on_delete=models.PROTECT)
    IsActive=models.BooleanField(default=1)
    def __str__(self):
        return str(self.ExamquestionId)







