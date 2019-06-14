from django.shortcuts import render

# Create your views here.
from .forms import RegistrationForm,LoginForm
from .models import rdata
from django.http.response import HttpResponse

def reg_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            fname=request.POST.get('fname','')
            lname=request.POST.get('lname','')
            uname=request.POST.get('uname','')
            pword=request.POST.get('pword','')
            mobile=request.POST.get('mobile','')
            email=request.POST.get('email','')
            data=rdata(fname=fname,
                       lname=lname,
                       uname=uname,
                       pword=pword,
                       mobile=mobile,
                       email=email,
                       )
            data.save()
            lform=LoginForm()
            return render(request,'login_form.html',{'lform':lform})
        else:
            return HttpResponse('invalid data')
    else:
        rform=RegistrationForm()
        return render(request,'reg_form.html',{'rform':rform})

def login_view(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            uname=request.POST.get('uname','')
            pword=request.POST.get('pword','')
            uname1=rdata.objects.filter(uname=uname)
            pwd1=rdata.objects.filter(pword=pword)
            if uname1 and pwd1:
                return HttpResponse('login successfully')
            else:
                return HttpResponse('user name or password is wrong')
        else:
            return HttpResponse('invalid data')
    else:
        lform=LoginForm()
        return render(request,'login_form.html',{'lform':lform})
