from django.shortcuts import render
import random
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password':'j4i1p34fjqilr'})


def password(request):

    characters = list('abcdefghijklmnopqrstuwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*-_=+?,.'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})


def credits(request):
    return render(request, 'generator/credits.html')
