from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LocalityForm, ResidenceForm, ResidentForm, EconomicActivityForm


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
            return redirect('menu')
        else:
            messages.warning(request, 'Error al agregar la localidad')
    else:
        local_form = LocalityForm()

    return render(request, 'wINEGI/locality.html', {
        'title': 'Localidad',
        'local_form': local_form,
    })

@login_required(login_url='login')
def residence(request):
    if request.method == 'POST':
        resicence_form = ResidenceForm(request.POST)
        if resicence_form.is_valid():
            resicence_form.save()
            messages.success(request, 'Vivienda agregada correctamente')
            return redirect('menu')
        else:
            messages.warning(request, 'Error al agregar la vivienda')
    else:
        resicence_form = ResidenceForm()

    return render(request, 'wINEGI/residence.html', {
        'title': 'Vivienda',
        'resicence_form': resicence_form,
    })

@login_required(login_url='login')
def resident(request):
    if request.method == 'POST':
        resident_form = ResidentForm(request.POST)
        if resident_form.is_valid():
            resident_form.save()
            messages.success(request, 'Habitante agregado correctamente')
            return redirect('menu')
        else:
            messages.warning(request, 'Error al agregar el habitante')
    else:
        resident_form = ResidentForm()

    return render(request, 'wINEGI/resident.html', {
        'title': 'Habitante',
        'resident_form': resident_form,
    })

@login_required(login_url='login')
def economic(request):
    if request.method == 'POST':
        economic_form = EconomicActivityForm(request.POST)
        if economic_form.is_valid():
            economic_form.save()
            messages.success(request, 'Actividad económica agregada correctamente')
            return redirect('menu')
        else:
            messages.warning(request, 'Error al agregar la actividad económica')
    else:
        economic_form = EconomicActivityForm()

    return render(request, 'wINEGI/economic.html', {
        'title': 'Actividad económica',
        'economic_form': economic_form,
    })