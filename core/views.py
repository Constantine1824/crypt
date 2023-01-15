from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from .models import User,PasswordModel

@login_required(login_url='login')
def index(request):
    
    if request.method == 'POST':
        current_user = request.user
        website,password,Username = request.POST['website'], request.POST['password'], request.POST['Username']
        field = PasswordModel.objects.create(user=current_user,hashedPw=password,website=website,username=Username)
        field.save()
        return redirect('/')
    
    else:
        username = request.user.username
        print(username)
        user_object = User.objects.get(username=username)
        password = PasswordModel.objects.filter(user=user_object)
        length = len(password)
        print(length)
        context = {
            'passw':password,
            'length':length
        }
        return render(request,'main.html',context)


def signUp(request):
    if request.method == 'POST':
        username,email,password,password2 = request.POST['username'],request.POST['email'],request.POST['password'],request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email already exists')
                return redirect('signup')
            else:
                current_user = User.objects.create(username=username,email=email,password=password)
                login(request,current_user)
                return redirect('/')
        else:
            messages.info(request,"Passwords don't match")
            return redirect('signup')
    return render(request,'signup.html')


def Login(request):
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user_object =authenticate(username=username,password=password) 
        if user_object is not None:
            current_user = User.objects.get(username=username)
            login(request,current_user)
            return redirect('/')
        else:
            messages.info(request,'username or password incorrect!')
            return redirect('/login')

    return render(request,'login.html')

# @login_required(login_url='login')
# def add(request):
#     if request.method == 'POST':
#         username,website,password = request.POST['username'],request.POST['website'],request.POST['password']
#         current_user = request.user
#         PasswordModel.objects.create(user=current_user,hashedPw=password,website=website,username=username)
#         return redirect('/')
        
#     else:
#         return render(request,'add.html')

@login_required(login_url='login')
def viewPass(request):
    id = request.GET.get('passwordId')
    pInfo = PasswordModel.objects.get(id=id)
    
    context = {
        'pInfo':pInfo
    }
    return render(request,'viewPassword.html',context)

# Create your views here.
