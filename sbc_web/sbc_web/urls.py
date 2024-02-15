# URL configuration for sbc_web project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from . import views as sbc_web_views
from django.contrib import admin
from django.urls import include
from django.urls import path
from perfiles import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('registro/', sbc_web_views.register, name='register'),
    path('logout/', sbc_web_views.cerrar_sesion, name='logout'),
    # path('', sbc_web_views.iniciar_sesion, name='signin'),
    path('perfiles/', include('perfiles.urls'), name='perfiles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

