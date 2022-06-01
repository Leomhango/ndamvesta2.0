# default imports
from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# my Imports
from .models import Word
from .forms import CreateUserForm, AddWordForm

# Not logged In
def index(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        word = Word.objects.order_by('word')
        context = {
            'word': word
        }
        return render(request, 'main/index.html', context)

def search(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
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

# Authentication
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
    return render(request, 'main/auth/signup.html', context)

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


        return render(request, 'main/auth/login.html')

def logoutUser(request):
    logout(request)
    return redirect('main:index')


# If user is logged in
@login_required(login_url='main:index')
def home(request):
    word = Word.objects.order_by('word')
    context = {
        'word': word
    }
    return render(request, 'main/dashboard/home.html', context)

@login_required(login_url='main:index')
def results(request):
    if request.method == "POST": 
        searched = request.POST['searched']
        word = Word.objects.filter(word__contains=searched)
        context = {
            'searched': searched,
            'words': word
        }
        return render(request, 'main/dashboard/search.html', context)
    else:
        return render(request, 'main/dashboard/search.html')

@login_required(login_url='main:index')
def dashbBoard(request):
    return render(request, 'main/dashboard/dashboard.html')

@login_required(login_url='main:index')
def addWord(request):
    form = AddWordForm

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()

            word = form.cleaned_data.get('word')
            messages.success(request, 'You added ' + word)

            return redirect('main:post')

    context = {
        'form': form
    }
    return render(request, 'main/dashboard/post.html', context)