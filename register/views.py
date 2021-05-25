from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core import mail
from django.contrib import messages
from django.template.loader import render_to_string
from .forms import RegisterForm
from decouple import config

email_destinatario = config('EMAIL_TO')
email_remetente = config('EMAIL_FROM')


def register(request):
    """Realize the signup user"""
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User has been registered successfully!")
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            body = render_to_string('register/email_signup.txt',
                                    form.cleaned_data)
            mail.send_mail('Sign up Confirmation',
                            body,
                            email_destinatario,
                            [email_remetente, form.cleaned_data['email']])
            
            return redirect('home')
        else:
            messages.error(request, 'Email or username already registered.')
            return render(request, 'register/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})


