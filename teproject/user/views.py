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

def result(request):
    return render(request,"user/result.html")

# def getPredictions(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q):
#     import pickle
#     model = joblib.load('xgboost.sav')
#     scaled = joblib.load('encoder.sav')
#     prediction = model.predict(le.transform([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q]]))
#     print(prediction)

# def result(request):
#     a = int(request.GET['a'])
#     b = int(request.GET['b'])
#     c = int(request.GET['c'])
#     d = int(request.GET['d'])
#     e = int(request.GET['e'])
#     f = int(request.GET['f'])
#     g = int(request.GET['g'])
#     h = int(request.GET['h'])
#     i = int(request.GET['i'])
#     j = int(request.GET['j'])
#     k = int(request.GET['k'])
#     l = int(request.GET['l'])
#     m = int(request.GET['m'])
#     n = int(request.GET['n'])
#     o = int(request.GET['o'])
#     p = int(request.GET['p'])
#     q = int(request.GET['q'])


#     result = getPredictions(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q)

#     return render(request, 'result.html', {'result':ans})