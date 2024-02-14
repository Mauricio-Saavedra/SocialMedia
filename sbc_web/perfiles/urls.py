from django.urls import register_converter
from django.urls import path
from . import views

# -------------------------- Clase para tener URL's sin espacios ------------------------
class SlugConverter:
    regex = r'[\w-]+'    # regex == regular expression, [1.-]
    # Recuerda poner '[\w-]+' como -> r'[\w-]+' ó '[\\w-]+'
    # Para que se interprete correctamente la barra.

    def to_python(self, value):         # 2.-
        return value.replace('-', ' ')

    def to_url(self, value):            # 3.-
        return value.replace(' ', '-')
# -------------------------- Clase para tener URL's sin espacios ------------------------

register_converter(SlugConverter, 'slug')   # 4.-


urlpatterns = [
    path('SBC/<int:id>/<slug:nombre>', views.SBC, name='SBC'),
    path('SBC/<int:id>/<slug:nombre>/e_e', views.editar_perfil, name='edit_sbc'),
    path('compartir/', views.obtener_url, name='obtener_url'),
]

# Explicación a mí mismo de la Clase SlugConverter:

# 1.- Esta línea define una variable de clase regex que contiene una expresión regular.
#     Esta expresión regular coincide con cualquier cadena que contenga letras, números, guiones bajos y guiones.
#     Los corchetes [] definen un conjunto de caracteres que pueden coincidir, \w coincide con cualquier carácter alfanumérico
#     o guion bajo, y - simplemente coincide con un guión. El signo más + al final significa que puede haber uno o más de estos caracteres.

# 2.- Este es el método to_python(). Se llama cuando Django extrae una variable de la URL. Toma la parte de la URL que coincide
#     con el patrón de la ruta (en este caso, una cadena que contiene letras, números, guiones bajos y guiones) y la convierte
#     en un tipo de dato Python. En este caso, el método to_python() simplemente reemplaza todos los guiones en la cadena con espacios.

# 3.- Este es el método to_url(). Se llama cuando Django construye una URL a partir de una vista. Toma un tipo de dato Python
#     (en este caso, una cadena) y lo convierte en una cadena que se puede usar en una URL. En este caso, el método to_url()
#     simplemente reemplaza todos los espacios en la cadena con guiones.

# 4.- Finalmente, esta línea registra el convertidor de ruta personalizado con Django. Esto permite que el convertidor de ruta
#     personalizado sea usado en las rutas de la URL con <slug:nombre>. register_converter() toma dos argumentos:
#     i:  el convertidor de ruta personalizado,
#     ii: un nombre corto para el convertidor de ruta personalizado.
#     En este caso, el nombre corto es 'slug'
