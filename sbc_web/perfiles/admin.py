from django.contrib import admin
from .models import Perfiles, ImagenLink

# Register your models here.

# Creando una clase para personalizar el panel de administración de Django y personalizando el panel de administrador.
@admin.register(Perfiles)
class PerfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'desc', 'imagen', 'vcf_file', 'links', 'telefonos')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre', 'desc', 'telefonos')
    list_per_page = 10
    list_max_show_all = 100
    readonly_fields = ('created', 'updated', 'user')

@admin.register(ImagenLink)
class ImagenLinkAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'LinkImg', 'LinkName')


