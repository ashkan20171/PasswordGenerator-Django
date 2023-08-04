from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')
def password(request):
    characters=list("qwertyuiopasdfghjklzxcvbnm")

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('symbols'):
        characters.extend(list('!@#$%^&*()_+'))
    thepassword=""
    length = int(request.GET.get('length'))
    for _ in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {"password":thepassword})