from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.files import File
from .models import Perfiles

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        with open('media/img/profile-placeholder.png', 'rb') as f:
            file = File(f)
            Perfiles.objects.get_or_create(
                user=instance,
                defaults={
                    'imagen': file,
                    'nombre': instance.username,
                    'desc': 'Haciendo contactos de calidad.',
                    'links': 'music.youtube.com/watch?v=b6e_wdtBVW8&list=RDAMVMb6e_wdtBVW8',
                    'telefonos': '5555555555',
                }
            )

# Este es el código que se ejecuta cuando se crea un usuario,
    # se crea un perfil automáticamente.
    # Como su nombre lo dice este archivo es para emitir señales, como en Godot.