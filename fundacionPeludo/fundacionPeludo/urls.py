"""fundacionPeludo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import appPeludo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appPeludo.views.home, name="home"),
    path('perros/', appPeludo.views.perros, name="perros"),
    path('gatos/', appPeludo.views.gatos, name="gatos"),
    path('acercade/', appPeludo.views.acercade, name="acercade"),
    path('cookie/', appPeludo.views.cookie, name="cookie"),
    path('daisy/', appPeludo.views.daisy, name="daisy"),
    path('kota/', appPeludo.views.kota, name="kota"),
    path('arbor/', appPeludo.views.arbor, name="arbor"),
    path('blizzard/', appPeludo.views.blizzard, name="blizzard"),
    path('bob/', appPeludo.views.bob, name="bob"),
    path('crearMascota/', appPeludo.views.crearMascota, name="crearMascota"),
    path('crearMascotaNav/<str:codigo>/<str:anios>/<str:nombre>/<str:especie>/<str:vacunado>/', appPeludo.views.crearMascotaNav, name="crearMascotaNav"),
    path('listarMascotas/', appPeludo.views.listar_mascotas, name="listarMascotas"),
    path('leerMascota/<int:id>', appPeludo.views.leer_mascota, name="leerMascota"),
    path('editarMascota/<int:id>', appPeludo.views.editar_mascota, name="editarMascota"),
    path('borrarMascota/<int:id>', appPeludo.views.borrar_mascota, name="borrarMascota"),

    path('nuevaMascota/', appPeludo.views.nuevaMascota, name="nuevaMascota"),
    path('guardarMascota/', appPeludo.views.guardarMascota, name="guardarMascota"),

    path('formMascota/', appPeludo.views.formMascota, name="formMascota"),
    path('formMascotaMod/<int:id>', appPeludo.views.formMascotaMod, name="formMascotaMod"),
    path('formMascotaDel/<int:id>', appPeludo.views.formMascotaDel, name="formMascotaDel"),
]
