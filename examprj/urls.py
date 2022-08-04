"""examprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from examapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', views.welcomeView, name="welcomeview"),
    path('examview',views.ExamdbView,name="examview"),
    path('listexam',views.listexamformview,name="listexam"),
    path('editexam/<str:examId>',views.EditExamdb,name="EditExamFrm"),
    path('createsubject',views.subjectdbView,name="CreateSubject"),
    path('listsubject',views.listsubject,name="ListSubject"),
    path('editsubject/<str:subjectId>',views.EditSubject,name="EditSubject"),
    path('deletesubject/<str:subjectId>',views.DeleteSubject,name="DeleteSubject"),
    path('createquestion',views.QuestiondbView,name="CreateQuestion"),
    path('listquestion',views.listquestions,name="ListQuestions"),
    path('editquestion/<str:sanjeev>',views.editquestions,name="EditQuestion"),
    path('searchquestions',views.searchquestions,name="SearchQns"),
    path('questionOptions',views.questionoptions,name="CreateOptions"),
    path('getquestions',views.getquestions,name="GetQuestions"),
    path('setquestions',views.setquestionpaper,name='SetQuestions'),
    path('showquestions',views.showquestions,name='ShowQuestions'),


]
