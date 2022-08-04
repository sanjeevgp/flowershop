from faulthandler import disable
from inspect import Attribute
from pickle import TRUE
from pyexpat import model
from tkinter import DISABLED
from xml.dom.minidom import Attr
from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import ModelForm
from examapp.models import examdb,subjectdb,questionsdb



class examdbmodelform(ModelForm):
    def __init__(self, *args, **kwargs):#constructor function and.This is called as a dunder function
        super().__init__(*args,**kwargs)# we are calling the constructor function of ModelForm too
        self.fields['ExamType']=forms.ChoiceField(widget=forms.Select, choices=((1,'Multiple Choice'),(2,'Descriptive'),(3,'CompAidedExam')))
        self.fields['ExamType'].widget.attrs.update({"class":"select2"})
       # self.fields['ExamYear']=forms.TextInput(attrs={"DISABLED":TRUE})
        self.fields['ExamDate'].widget.attrs.update({'type': 'date',"class" :"datepicker"})
        #self.fields['ExamDate']=forms.DateField()
        self.fields['ExamYear'].widget.attrs.update({'readonly':True})
    class Meta:
        model=examdb
        exclude=('ExamId',)

class subjectdbmodelform(ModelForm):
    class Meta:
        model=subjectdb
        exclude=('SubjectId',)

class questionsdbmodelform(ModelForm):
    def __init__(self, *args, **kwargs):#constructor function and.This is called as a dunder function
        super().__init__(*args,**kwargs)# we are calling the constructor function of ModelForm too
        self.fields['QuestionType']=forms.ChoiceField(widget=forms.Select, choices=(("Multiple Choice",'Multiple Choice'),("Descriptive",'Descriptive'),("CompAidedExam",'CompAidedExam')))
        self.fields['Questions']=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':40}))
    class Meta:
        model=questionsdb
        exclude=('QuestionId','IsActive')


        