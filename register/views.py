from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.core import mail
from django.contrib import messages
from django.template.loader import render_to_string
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from decouple import config

def register(request):
    """Realize the signup user"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email_from = config('EMAIL_FROM')
            form.save()
            messages.success(request, "User has been registered successfully!")
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            body = render_to_string('register/email_signup.txt',
                                    form.cleaned_data)
            mail.send_mail('Sign up Confirmation',
                            body,
                            email_from,
                            [email_from, form.cleaned_data['email']])
            
            return redirect('profile')
        else:
            messages.error(request, 'Email or username already registered.')
            return render(request, 'register/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})

@login_required(login_url='/login/')
def profile(request):
    """Get more information about just registered user"""
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Thank you!')
            return redirect('core:home')
        else:
            messages.error(request, 'Please review the information you are trying to submit.')
            return render(request, 'register/infos.html', {'form': form})
    else:
        form = ProfileForm()
    return render(request, 'register/infos.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, 'You have been logged successfully.')
                return redirect('core:home')
        else:
            messages.error(request,'Username or Password not correct')
            return redirect('login')

    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logouted successfully.')
    return redirect('login')