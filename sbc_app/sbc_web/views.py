from django.shortcuts import render, redirect
from django.db import IntegrityError    # Esto es para que no se puedan crear dos usuarios con el mismo nombre.
from django.contrib.auth import login, logout, authenticate   # Esto es para que el usuario se loguee automáticamente tras registrarse.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from perfiles.models import Perfiles

def register(request):  # Esta función es para registrar usuarios, nada más.
    conflicto = False

    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'register.html', {
                'form': UserCreationForm(),
                'error': 'Las contraseñas no coinciden.',
                'conflicto': True,
                })
        else:
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {
                    'form': UserCreationForm(),
                    'error': 'Ese nombre de usuario ya está en uso.',
                    'conflicto': True,
                })
            else:
                user = User.objects.create_user(username=username, password=request.POST['password1'])
                perfil = Perfiles.objects.get(user=user)
                login(request, user)
                return redirect('SBC', id=perfil.id, nombre=perfil.nombre)


def iniciar_sesion(request):    # Esta función es para iniciar sesión con un usuario previamente registrado.
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm,
            })
    else:
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
            )
        if user is not None:
            login(request, user)
            perfil = Perfiles.objects.get(user=user)
            return redirect('SBC', id=perfil.id, nombre=perfil.nombre) 
        else:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Nombre de usuario o contraseña incorrectos.',
                'conflicto': True,
                })


def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)
        return redirect('register')
    else:
        return redirect('register')

