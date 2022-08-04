from django.contrib import admin

from examapp.models import examdb,subjectdb,examquestiondb,optionsdb,questionsdb,answeresdb

# Register your models here.

admin.site.register (examdb)
admin.site.register(subjectdb)
admin.site.register(examquestiondb)
admin.site.register(optionsdb)
admin.site.register(answeresdb)
admin.site.register(questionsdb)

