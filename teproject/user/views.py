from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import os
import joblib
  
#################### index#######################################
def index(request):
    return render(request, 'user/index.html', {'title':'index'})
  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'reqister here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})

################ import ml###################################################
from xgboost import XGBClassifier
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def result(request):
    return render(request,"user/result.html")

def getPredictions(arr):
    #import pickle
    model = joblib.load('extra.sav')
    #scaled = joblib.load('encoder.sav')
    prediction = model.predict(arr)
    return prediction

def result(request):
    if request.method=='POST':
        a = int(request.POST.get('a'))
        b = int(request.POST.get('b'))
        c = int(request.POST.get('c'))
        d = int(request.POST.get('d'))
        e = int(request.POST.get('e'))
        f = int(request.POST.get('f'))
        g = int(request.POST.get('g'))
        h = int(request.POST.get('h'))
        i = int(request.POST.get('i'))
        j = int(request.POST.get('j'))
        k = int(request.POST.get('k'))
        l = int(request.POST.get('l'))
        m = int(request.POST.get('m'))
        n = int(request.POST.get('n'))
        o = int(request.POST.get('o'))
        p = int(request.POST.get('p'))
        q = int(request.POST.get('q'))

        arr = ([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q]])
        print(arr)

        ans = getPredictions(arr)        
        
        if ans[0]==0:
            recommend="Automobile Engineering"

        elif ans[0]==1:
            recommend="Banking"

        elif ans[0]==2:
             recommend="Chartered Accountant"

        elif ans[0]==3:
            recommend="Civil Engineering"

        elif ans[0]==4:
            recommend="Civil Services"
        
        elif ans[0]==5:
            recommend="Interior Designer"

        elif ans[0]==6:
            recommend="Lawyer"

        elif ans[0]==7:
            recommend="Management Studies"

        elif ans[0]==8:            
            recommend="Marketing Studies"

        elif ans[0]==9:            
            recommend="Mass Media"
        
        elif ans[0]==10:
            recommend="Mechanical Engineering"
            
        
        elif ans[0]==11:
            recommend="Medical Science"
            

        elif ans[0]==12:
            recommend="Pharmacist"
        
                 

        elif ans[0]==13:
            recommend="Pilot"
            
        
        elif ans[0]==14:
            recommend="Scientist"
            

        elif ans[0]==15:
            recommend="Software Engineering"
            
        
        elif ans[0]==16:
            recommend="Teacher"

        else: 
            recommend="Error, please go back and answer questions again."
            
    

        # if (ans[0]==7):
        #     print (ans[0])
        #     recommend="Management Studies"

        return render(request, 'user/result.html', {'ans': recommend})

    # else:
    #     return render(request,'user/result.html' , {'ans': ans})