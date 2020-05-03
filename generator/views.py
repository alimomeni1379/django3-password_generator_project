from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    char=list(('abcdefghijklmnopqrstuvwxyz'))
    if request.GET.get('number'):
        char.extend('1234567890')
    if request.GET.get('word'):
        char.extend('!@#$%^&*()')
    if request.GET.get('uppercase'):
        char.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    ran=12
    word =''
    for cahracter in range(ran):
        word+= random.choice(char)
    return render(request,'generator/password.html',{'password':word})
