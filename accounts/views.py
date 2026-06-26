from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import RegistoForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio_index')
        else:
            return render(request, 'accounts/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('portfolio_index')

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            user = form.save()
            grupo, _ = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo)
            return redirect('login')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})