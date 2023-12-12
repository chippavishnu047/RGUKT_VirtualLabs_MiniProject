from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from app1.models import Student
from django.contrib.auth import logout
from django.contrib import messages
from app1.models import QuesModel,res,Question,DBMS,Pyy,Py_res,DB_res
n='rgukt'
def home(request):
    return render(request,'home.html')
def signin(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['pass1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Login successfull")
            return redirect("/")
        else:
            print("UnSuccessfull")
            messages.info(request,"No user found/Invalid Credentials")
            return redirect("/")
    else:
        return render(request,'signin.html')
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if (pass1==pass2):
            if (User.objects.filter(username=username).exists()):
                messages.info(request,"Username already taken")
                return redirect('/') 
            elif (User.objects.filter(email=email).exists()):
                messages.info(request,"Email already taken")
                return redirect('/') 
            else:
                myuser=User.objects.create_user(username,email,pass1)
                myuser.save()
                return redirect('signin')
            
        else:
            messages.info(request,"Password not matching")
            return redirect('/') 
    else:
        return render(request,'register.html')
def user_logout(request):

        logout(request)
        messages.success(request,"Logout successfull")
        return redirect('/')
def home2(request):
    print("Entered")
    if (request.user.id==None):
        messages.info(request,"Please Login to access the course")

        return redirect('/')
       
    else:
        return render(request,'topic.html')
def home3(request):
    print("Entered")
    if (request.user.id==None):
        messages.info(request,"Please Login to access the course")

        return redirect('/')
       
    else:
        return render(request,'DBtopic.html') 
def python(request):
    print("Entered")
    if (request.user.id==None):
        messages.info(request,"Please Login to access the course")

        return redirect('/')
       
    else:
        return render(request,'python.html')
def temp(request):
    if request.method == 'POST':
        print(request.user.id)
        name=User.objects.all().get(id=request.user.id)
        #print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print("Anser ",q.ans)
            print()
            if q.ans ==  (request.POST.get(q.question)):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        print("user id",request.user.id)
        print(User.objects.all().values())
       # print(u)
       
        r=res(name=name,marks=score)
        r.save()
        name=str(name)
        context = {
            'name':name.capitalize(),
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'home2.html',context)
def basicsyntax(request):
    return render(request,'basicsyntax.html')
def code(request):
    return render(request,'compile.html')
def practice(request):
    questions=Question.objects.all()
    print(questions)
    context = {
            'questions':questions
        }
    return render(request,'practice.html',context)
def dbbasic(request):
    return render(request,'DBbasicsyntax.html')
def pbasic(request):
    return render(request,'python.html')
def pcontent(request):
    return render(request,'pythonbasic.html')
def quiz(request):
    if request.method == 'POST':
        # print(request.user.id)
        name=User.objects.all().get(id=request.user.id)
        #print(request.POST)
        questions=DBMS.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print()
            if q.ans ==  (request.POST.get(q.question)):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        # print("user id",request.user.id)
        # print(User.objects.all().values())
       # print(u)
       
        r=DB_res(name=name,marks=score)
        r.save()
        name=str(name)
        context = {
            'name':name.capitalize(),
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions=DBMS.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'dbquiz.html',context)
def pquiz(request):
    if request.method == 'POST':
        # print(request.user.id)
        name=User.objects.all().get(id=request.user.id)
        #print(request.POST)
        questions=Pyy.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print()
            if q.ans ==  (request.POST.get(q.question)):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        # print("user id",request.user.id)
        # print(User.objects.all().values())
       # print(u)
       
        r=Py_res(name=name,marks=score)
        r.save()
        name=str(name)
        context = {
            'name':name.capitalize(),
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions=Pyy.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'dbquiz.html',context)


