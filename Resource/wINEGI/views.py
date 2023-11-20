from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LocalityForm


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Bienvenido has iniciado sesion')
            return redirect('menu')

        else:
            messages.warning(request, 'Password o usuario incorrecto!')


    return render(request, 'users/login.html',{
        'title': 'Login'
    })

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def menu (request):
    return render(request, 'wINEGI/menu.html', {
        'title': 'Menu',
    })

@login_required(login_url='login')
def locality(request):
    if request.method == 'POST':
        local_form = LocalityForm(request.POST)
        if local_form.is_valid():
            local_form.save()
            messages.success(request, 'Localidad agregada correctamente')
            return redirect('locality')
        else:
            messages.warning(request, 'Error al agregar la localidad')
    else:
        local_form = LocalityForm()

    return render(request, 'wINEGI/locality.html', {
        'title': 'Localidad',
        'local_form': local_form,
    })
