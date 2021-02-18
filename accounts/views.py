from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        login_var = AuthenticationForm(data=request.POST)
        if login_var.is_valid():
            # log in the user
            user = login_var.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')

    else:
        login_var = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_var': login_var})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')




