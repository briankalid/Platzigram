from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#User views
# Create your views here.

from .models import Profile

#Exceptions
from django.db.utils import IntegrityError

from .forms import Userform

def login_view(request):
    profile = request.user
    if request.method == "POST":
        #username = request.POST['username']
        #password = request.POST['password']

        form = Userform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data

            username = data['username']
            password = data['password']

            user = authenticate(request,username=username,password=password)
            
            if user:
                login(request,user)
                return redirect('feed')
            else:
                return render(request,'users/login.html', {'error':'Invalid username or password'})
    else:
        form = Userform()

    if not request.user.is_authenticated:
        return render(request,'users/login.html',context={'form':form})
        #form = Userform()
    else:
        return redirect('feed')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirm = request.POST['passwd_confirmation']

        if passwd != passwd_confirm:
            return render(request,'users/signup.html',{'error':'Password passwd_confirmation does not match'})


        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        try:
            user = Profile.objects.create_user(username=username,password=passwd,first_name=first_name,last_name=last_name,email=email)
    
        except IntegrityError:
           return render(request,'users/signup.html',{'error':'Usename is already in use'})
 

        user = authenticate(request,username=username,password=passwd)

        if user:

            login(request,user)
            return redirect('feed')

        else:
            return redirect('login')


    if not request.user.is_authenticated:

        return render(request,'users/signup.html')
    else:
        return redirect('feed')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
