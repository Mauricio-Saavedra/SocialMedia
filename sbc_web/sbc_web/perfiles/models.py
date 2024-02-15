from django.db import models
from django.contrib.auth.models import User

# Obteniendo el usuario por defecto.
def default_user():
    return User.objects.get_or_create(username='default').id


# Create your models here.
class Perfiles(models.Model):
    imagen = models.ImageField(upload_to='img/', verbose_name='Imagen')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    desc = models.CharField(max_length=100, verbose_name='Descripción')
    vcf_file = models.FileField(upload_to='vcf_files/', blank=True, null=True, verbose_name='Archivo VCF')
        # Sección del modelo que guardará los links de las redes sociales en un campo de texto que se tiene que convertir a una lista.
    links = models.TextField(blank=True, null=True, verbose_name='Links')
        # Sección del modelo que guardará los números de teléfono en un campo de texto que se tiene que convertir a una lista.
    telefonos = models.TextField(blank=True, null=True, verbose_name='Teléfonos')
        # Sección de la temporalidad de los datos.
    created = models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    # Sección del modelo que relaciona el perfil con el usuario, aka ForeignKey.
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=default_user, verbose_name='Usuario', unique=True)


class ImagenLink(models.Model):
    perfil = models.ForeignKey(Perfiles, on_delete=models.CASCADE)
    LinkImg = models.ImageField(upload_to='img/', verbose_name='User_Link_Image')
    LinkName = models.CharField(max_length=100, verbose_name='User_Link_Name')

    class Meta:
        verbose_name = 'User_Image'
        verbose_name_plural = 'User_Image'
