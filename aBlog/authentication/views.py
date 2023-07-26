from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def SignupView(request): 
    normalUser = ''
    admin = ''
    if request.method == 'POST':
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')

        if password1 != password2:
            return messages.error(request, 'Password Doesn\'t match!')
        else:
            my_user = User.objects.create_user(first_name=firstName,last_name=lastName,email=email,username=username,password=password1)
            my_user.save()
            return redirect('login')

            # if admin:
            #     my_user = User.objects.create_user(first_name=firstName,last_name=lastName,email=email,username=username,password=password1)
            #     my_user.save()
            #     return redirect('login')
            # elif normalUser:
            #     my_user = User.objects.create_user(firsName=firstName,lastName=lastName,email=email,username=username,password=password1)
            #     my_user.save()
            #     return redirect('login')

    return render(request, 'authentication/signup.html')

def LoginView(request):
    normalUser = ''
    admin = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username=username, password=password)
        
        if my_user is not None:
            login(request, my_user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credentials!')

        # if my_user is not None and admin:
        #     login(request, my_user)
        #     return redirect('admin')
        # elif my_user is not None and normalUser:
        #     login(request, my_user)
        #     return redirect('home')
        # else:
        #     messages.error(request, 'Wrong Credentials!')

    return render(request, 'authentication/login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')
