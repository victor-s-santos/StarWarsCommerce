from django.shortcuts import render

def index(request):
    return render(request, 'commerce.html')
# Create your views here.
