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
        return create(request)
    else:
        return new(request)

def create(request):
    form = RegisterForm(request.POST)
    if not form.is_valid():
        messages.error(request, 'Email or username already registered.')
        return render(request, 'register/register.html', {'form': form})
    #send email
    form.save()
    _send_email("User has been registered successfully!",
                config('EMAIL_FROM'),
                form.cleaned_data['email'],
                'register/email_signup.txt',
                form.cleaned_data
                )
    username = form.cleaned_data.get('email')
    raw_password = form.cleaned_data.get('password1')
    #login_user
    _login_user(request, username, raw_password)
    messages.success(request, "User has been registered successfully!")
    return redirect('profile')

def _login_user(request, username, raw_password):
    user = authenticate(username=username, password=raw_password)
    auth_login(request, user)
    
        
def _send_email(subject, email_from, to, template_name, context):
        body = render_to_string(template_name, context)
        mail.send_mail(subject, body, email_from, [email_from, to])

def new(request):
    form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})

@login_required(login_url='/login/')
def profile(request):
    """Get more information about just registered user"""
    if request.method == "POST":
        return create_profile(request)
    else:
        return new_profile(request)

@login_required(login_url='/login/')
def create_profile(request):
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
    
def new_profile(request):
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