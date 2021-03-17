from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError

# def signupuser(request):
#     return render(request, 'members/signupuser.html', {'form':UserCreationForm()})


#Signup function
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'members/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                login(request, user)
                messages.success(request, 'User Registered Successfully.')
                return redirect('signupuser')
            except IntegrityError:
                return render(request, 'members/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'members/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

