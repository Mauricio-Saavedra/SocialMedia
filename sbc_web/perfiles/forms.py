from django.forms import ModelForm
from .models import Perfiles, ImagenLink

class ProfileForm(ModelForm):
    class Meta:
        model = Perfiles
        fields = ['imagen','desc','links','telefonos']

class LinkForm(ModelForm):
    class Meta:
        model = ImagenLink
        fields = ['LinkImg', 'LinkName']
