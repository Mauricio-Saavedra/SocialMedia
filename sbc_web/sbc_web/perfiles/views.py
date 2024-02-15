from django.shortcuts import render, redirect
from .models import Perfiles
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

def Mauricio_Saavedra(request):
    nombre = 'Mauricio Saavedra'
    desc = 'Escritor de Código y Literatura'
    web_links = [
        'linkedin.com/in/original-mauricio-saavedra/',
        'github.com/Mauricio-Saavedra',
        'amazon.com.mx/dp/B0BRLFZP7V?ref_=cm_sw_r_cp_ud_dp_6W2SCJKZ2NB8SSNV6H09',
        'twitter.com/_MauSaavedra',
        'music.youtube.com/playlist?list=OLAK5uy_lYdwxvfKoDIiUba2_Dh1Pc-zOLLANCwKY',
        ]
    datos = {
        'nombre' : nombre,
        'desc'   : desc,
    }
    return render(request, 'mauricio.html', {'datos': datos, 'web_links': web_links})
        # Esto pasa los datos y los links a la plantilla.

@login_required
def SBC(request, id, nombre):
    datos = Perfiles.objects.get(id=id) # Esto obtiene los datos del perfil con el id que se le pasa por parámetro.
    nombre = Perfiles.objects.get(nombre=nombre) 
    web_links = datos.links.split(',')  # Esto convierte el string de links en una lista.
    print(request.user, datos.user.id)
    return render(request, 'sbc.html', {'datos': datos, 'web_links': web_links})
        # Esto pasa los datos y los links a la plantilla.

@login_required
def editar_perfil(request, id, nombre):
    perfil = Perfiles.objects.get(id=id)
    if request.method == 'GET':
        form = ProfileForm(instance=perfil)
        return render(request, 'edit_sbc.html', {'form': form})
    else:
        form = ProfileForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('SBC', id=id, nombre=nombre)
        else:
            return render( request, 'edit_sbc.html', {
                'form': form,
                'error': 'Los datos no son válidos.'
                })

from django.http import JsonResponse

def obtener_url(request):
    actual_url = request.build_absolute_uri()
    return JsonResponse({'actual_url': actual_url})
