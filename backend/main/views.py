# default imports
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# my Imports
from .models import Word
from .forms import CreateUserForm

def index(request):
    word = Word.objects.order_by('word')
    context = {
        'word': word
    }
    return render(request, 'main/index.html', context)

@login_required(login_url='main:index')
def home(request):
    word = Word.objects.order_by('word')
    context = {
        'word': word
    }
    return render(request, 'main/dashboard/home.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Has Been Created For ' + user +' . Now You Can Log In')

                return redirect('main:login')


    context = {
        'form': form
    }
    return render(request, 'main/signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main:home')


        return render(request, 'main/login.html')

def logoutUser(request):
    logout(request)
    return redirect('main:index')

def post(request):
    return render(request, 'main/post.html')

def search(request):
    if request.method == "POST": 
        searched = request.POST['searched']
        word = Word.objects.filter(word__contains=searched)
        context = {
            'searched': searched,
            'words': word
        }
        return render(request, 'main/search.html', context)
    else:
        return render(request, 'main/search.html')
