from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import auth
from mainscrap.models import Data

def logingin(request):

    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/signup')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name','')
        first_name = request.POST.get('first_name','')
        last_name = request.POST.get('last_name','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-Mail Already Exist Please Use Different Email')
        else:
            user = User.objects.create_user(user_name, email, password)
            user.is_active = True
            user.first_name = first_name
            user.last_name = last_name
            user.save()
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)

    if logout:
        return redirect('/login')
    return render(request, "logout.html")

def accounts(request):
    main_data = Data.objects.all()
    #parms = {}
    return render(request, 'accounts.html',{'name' : request.user.username, 'main_data': main_data})