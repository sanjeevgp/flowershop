from pickle import GET
from re import template
from traceback import print_list
from xml.dom.expatbuilder import TEXT_NODE
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render

from .forms import examdbmodelform,subjectdbmodelform,questionsdbmodelform
from .models import examdb,subjectdb,questionsdb,optionsdb,answeresdb,examquestiondb

# Create your views here.

def welcomeView(request):
    template_name="examapp/welcome.html"
    return HttpResponse('Hi Welcome to Django')

def ExamdbView(request):
    template_name="examapp/exam.html"
    if request.method=="GET":
        examform = examdbmodelform()
        return render(request,template_name,context={"myform":examform,"anotherkey":"this is another key"})
    elif request.method=="POST":
        examform=examdbmodelform(request.POST)
        if examform.is_valid():
            print (examform)
            examform.save()
        return render(request,template_name,context={"exam_form":examform})


def listexamformview(request):
    template_name="examapp/listexamformview.html"
    if request.method=="GET":
        examlist=examdb.objects.all()
        return render(request,template_name,{"listexam":examlist})

def EditExamdb(request,examId=0):
    template_name="examapp/exam.html"
    objectExam=examdb.objects.get(ExamId=examId)
    if request.method =="GET":
        objexamform=examdbmodelform(instance=objectExam)
        return render(request,template_name,context={"myform":objexamform})
    elif request.method=="POST":
        objexamform=examdbmodelform(request.POST,instance=objectExam)
        if objexamform.is_valid():
            objexamform.save()
        return render(request,template_name,context={"myform":objexamform})
    

def subjectdbView(request):
    template_name="examapp\subjectForm.html"
    if request.method=="GET":
        subjectform =subjectdbmodelform()
        return render(request,template_name,context={"subjectForm":subjectform})
    elif request.method=="POST":
        subjectform=subjectdbmodelform(request.POST)
        if subjectform.is_valid():
            subjectform.save()
            subjectform =subjectdbmodelform()

            return render(request, template_name, context={"subjectForm":subjectform,"Successfullmsg":"This subject is created successfully" })
        else:
            return render(request,template_name, context={"subjectForm":subjectform} )

def EditSubject(request,subjectId=0):
    template_name="examapp/subjectForm.html"
    objectSubject=subjectdb.objects.get(SubjectId=subjectId)
    if request.method=="GET":

        subjectform=subjectdbmodelform(instance=objectSubject)
        return render(request, template_name,context={"subjectForm":subjectform})
    elif request.method=="POST":
        subjectform=subjectdbmodelform(request.POST,instance=objectSubject)
        if subjectform.is_valid():
            subjectform.save()
            return render(request,template_name,context={"subjectForm":subjectform})

def listsubject(request):
    template_name="examapp/listsubjectformview.html"
    subjectlist=subjectdb.objects.all()
    return render(request,template_name,context={"listsubject":subjectlist})

def DeleteSubject(request,subjectId):
    template_name="examapp/deletesubjectform.html"
    subjectinstance=subjectdb.objects.get(SubjectId=subjectId)
    if request.method =="GET":
        subjectinstance=subjectdb.objects.get(SubjectId=subjectId)
        return render(request,template_name,context={"SubjInstance":subjectinstance})
    elif request.method == "POST":
        subjectid=request.POST.get('subjectId')
        print(subjectid)
        subjectinstance=subjectdb.objects.get(SubjectId=subjectId)
        subjectinstance.delete()
        template_name="examapp/listsubjectformview.html"
        subjectlist=subjectdb.objects.all()
        return render(request,template_name,context={"listsubject":subjectlist})
        #subjectinstance=subjectdb(request.POST,instance=subjectinstance)
    

def QuestiondbView(request):
    template_name="examapp/questionsformview.html"
    if request.method=="GET":
        questionsform=questionsdbmodelform()
        return render(request,template_name,context={"questionForm":questionsform})
    elif request.method=="POST":
        questionsform=questionsdbmodelform(request.POST)
        if questionsform.is_valid():
            questionsform.save()
            questionsform=questionsdbmodelform()
            return render(request, template_name,context={"questionForm":questionsform})
        else:
            return render(request,template_name,context={"questionForm":questionsform})

def listquestions(request):
    template_name="examapp/listquestions.html"
    questionslist=questionsdb.objects.all()
    print (questionslist)
    return render(request,template_name,context={"listquestions":questionslist})

def editquestions(request,sanjeev=0):
    template_name="examapp/questionsformview.html"
    objectQuestion=questionsdb.objects.get(QuestionId=sanjeev)
    if request.method=="GET":
        questionsform=questionsdbmodelform(instance=objectQuestion)
        return render (request,template_name,context={"questionForm":questionsform})
    else:
        questionsform=questionsdbmodelform(request.POST,instance=objectQuestion)
        if questionsform.is_valid():
            questionsform.save()
            template_name="examapp/listquestions.html"
            questionslist=questionsdb.objects.all()
            return render (request,template_name,context={"listquestions":questionslist})
        else:
            return render (request,template_name,context={"questionForm":questionsform}) 
           

    
def searchquestions(request):
    template_name="examapp/searchsubject.html"
    if request.method=="GET":
        return render (request, template_name)
    elif request.method=="POST":
        subjectname=request.POST.get("SubjectName")
        listquestions=questionsdb.objects.filter(Subject__subject__contains=subjectname)
        print (listquestions)
        return render(request, template_name,context={'listquestion':listquestions})

def questionoptions(request):
    template_name="examapp/QuestionOptions.html"
    if request.method=="GET":
        subjectlist=subjectdb.objects.all()
        return render(request,template_name,context={'subjectlist':subjectlist})
    elif request.method=="POST":
        questionid=request.POST.get('Questions')
        optionsdbobj=optionsdb()
        questionobj=questionsdb.objects.get(QuestionId=questionid)
        optionsdbobj.Options= request.POST.get('option1')       
        optionsdbobj.QuestionId=questionobj
        optionsdbobj.save()
        optionsdbobj=optionsdb()
        optionsdbobj.Options= request.POST.get('option2')
        optionsdbobj.QuestionId=questionobj
        optionsdbobj.save()
        optionsdbobj=optionsdb()
        optionsdbobj.Options= request.POST.get('option3')
        optionsdbobj.QuestionId=questionobj
        optionsdbobj.save()
        optionsdbobj=optionsdb()
        optionsdbobj.Options= request.POST.get('option4')
        optionsdbobj.QuestionId=questionobj
        optionsdbobj.save()
         
        answeresdbobj=answeresdb()
        answeresdbobj.questionid=questionobj
        optionvalue = request.POST.get('answer')
        if optionvalue=="1":
            optionstring=request.POST.get('option1')
            optioobj=optionsdb.objects.filter(Options=optionstring,QuestionId=questionobj)
        elif optionvalue=="2":
            optionstring=request.POST.get('option2')
            optioobj=optionsdb.objects.filter(Options=optionstring,QuestionId=questionobj) 
        elif optionvalue=="3":
            optionstring=request.POST.get('option3')
            optioobj=optionsdb.objects.filter(Options=optionstring,QuestionId=questionobj)
        elif optionvalue=="4":
            optionstring=request.POST.get('option4')
            optioobj=optionsdb.objects.filter(Options=optionstring,QuestionId=questionobj)            
        answeresdbobj=answeresdb()
        answeresdbobj.QuestionId=questionobj
        print(questionobj.QuestionId)
        answeresdbobj.OptionsId=optioobj[0]
        answeresdbobj.save()

        subjectlist=subjectdb.objects.all()
        return render(request,template_name,context={'subjectlist':subjectlist})


def getquestions(request):
    typestring=request.GET.get('type')
    typestringval=''
    if typestring=="1":
        typestringval="Descriptive"
    elif typestring =='2':
        typestringval="Multiple Choice"
    elif typestring=="3":
        typestringval="CompAidedExam"

    subjectid=request.GET.get('subject')
    objsubject=subjectdb.objects.get(SubjectId=subjectid)
    questionlist=dict(questionsdb.objects.filter(Subject=objsubject,QuestionType=typestringval).values_list('QuestionId','Questions'))
    print(questionlist)
    return JsonResponse(questionlist,safe=False)

    

def setquestionpaper(request):
    template_name="examapp/QuestionPaperSetup.html"
    if request.method=='GET':
        examlist=examdb.objects.all()
        subjectlist=subjectdb.objects.all()
        return render(request,template_name,context={'examlist':examlist,'subjectlist':subjectlist})
    elif request.method=="POST":
        print('hello')
        print(request.POST)
        # examqnobj=examquestiondb()
        examid=request.POST.get('exam')
        examobj=examdb.objects.get(ExamId=examid)
        questionlist=request.POST.getlist('sanjeev') #for example 6,9 in questionlist we have 6 and 9.To save both we need to
        # loop through the list and take each question and save
        examquestiondb.objects.filter(Questions__QuestionId__in=questionlist).delete()

        for item in questionlist:
            examqnobj=examquestiondb()
            
            examqnobj.Exam=examobj
            #finding out the question object with the id contained in the item variable
            questionobj=questionsdb.objects.get(QuestionId=item)
            examqnobj.Questions=questionobj
            examqnobj.save()
        return render(request, template_name)




def showquestions(request):
    template_name="examapp/QuestionPaperSetup.html"
    if request.method=="GET":
        subjectid=request.GET.get('subject')
        objsubject=subjectdb.objects.get(SubjectId=subjectid)
    
        examid=request.GET.get('exam')
        objexam=examdb.objects.get(ExamId=examid)
        examtypeid=request.GET.get('examtype')
        existingqnlist=dict(examquestiondb.objects.filter(Exam=objexam).values_list("Questions__QuestionId",'Questions__Questions')) # __ fetching details from another db using foreign key
        #existingqnlist01=examquestiondb.objects.filter(Exam=objexam).values_list('Questions')
        
        originalqnlist=questionsdb.objects.filter(Subject=objsubject,QuestionType=examtypeid).values_list('QuestionId','Questions')
        questionlist=dict(questionsdb.objects.filter(Subject=objsubject,QuestionType=examtypeid).values_list('QuestionId','Questions'))

        if len(existingqnlist)==0:     

            questionlist=dict(questionsdb.objects.filter(Subject=objsubject,QuestionType=examtypeid).values_list('QuestionId','Questions'))
            #print(questionlist)
            dictcombined={'remaining':questionlist}
            return JsonResponse(dictcombined,safe=False)
        elif len(existingqnlist)>0:
            differenceqnlist=dictdifference(questionlist,existingqnlist)
            #print(differenceqnlist)
            #print(existingqnlist)
            #print(questionlist)
            #print(objexam)
            #print(existingqnlist01)
            dictcombined={'existing':existingqnlist,'remaining':differenceqnlist}
            print((dictcombined))
            return JsonResponse(dictcombined,safe=False)

def dictdifference(firstdict,seconddict):
    diff = firstdict.keys()-seconddict.keys()
    new_dict={k:firstdict[k] for k in diff}
    return new_dict





    








