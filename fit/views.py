from django.shortcuts import render,redirect
from .forms import  *
from .models import *
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm
# Create your views here.
def home(request):
    return render(request,"fit/index.html",{}) #return home page i.e index.html
def category(request):
    obj = Person.objects.all().filter(user=request.user)  #return category page
    obj = obj.order_by('-id')
    l = obj.first()
    l.bmi = l.weight / (l.height ** 2)
    l.save()
    if l.bmi < 18.5:
        c = 'under_weig'
    elif l.bmi < 25:
        c = 'Normal'
    else:
        c = 'Over_weigh'
    cat = Cataegory_tips.objects.get(category=c)
    z = cat.mortips.all()
    return render(request,"fit/category.html",locals())
def tips(request):                                               #displays exercises and diet acccrding to the category of the user
    obj=Person.objects.all().filter(user=request.user)
    obj=obj.order_by('-id')
    l=obj.first()
    l.bmi=l.weight/(l.height**2)
    l.save()
    if l.bmi<18.5:
        c='under_weig'
    elif l.bmi<25:
        c='Normal'
    else:
        c='Over_weigh'
    cat=Cataegory_tips.objects.get(category=c)
    z=cat.mortips.all()
    return render(request,"fit/tips.html",locals())
def contact(request):                                           #contact numbers of developers
    return render(request,"fit/contact.html",{})
def about(request):                                             #purpose
    return render(request,"fit/about.html",)
def input(request):                                             #take input for new users
    form=inputform()
    if request.method=='POST':
        form=inputform(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.user=request.user
            a.save()
            return redirect('tips')
    return render(request,'registration/login.html',locals())

def login_view(request):                                       #login the registered users
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/home')

    context = {
        'form': form,
    }
    return render(request, "fit/signin.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/home/input')

    context = {
        'form': form,
    }
    return render(request, "fit/signup.html", context)


def logout_view(request):                                   #logout
    logout(request)
    return redirect('/')

def feedlink(request):                                      #feeds
    return HttpResponse("Hello")

def dummy(request):                                         #sql query
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM fit_person''')
    row=cursor.fetchall()
    return render(request,'fit/cursortemp.html',{'p':row})