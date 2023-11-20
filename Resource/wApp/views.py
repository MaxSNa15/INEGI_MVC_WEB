from django.shortcuts import render

def index(request):
    return render(request, 'wApp/index.html', {
        'title': 'Inicio',
        'say': 'Bienvenido al sitio INEGI'
    })