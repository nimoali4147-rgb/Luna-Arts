from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html',{'form': forms})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                'Welcome to Luma Art! Your account has been created.'
            )
            return redirect('home')
    else:
        form = RegisterForm()

    return render(
        request,
        'photo_gallery/register.html',
        {'form': form}
    )

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Welcome back to Luma Art!')
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(
        request,
        'photo_gallery/login.html',
        {'form': form}
    )


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have logged out successfully.')

    return redirect('login')