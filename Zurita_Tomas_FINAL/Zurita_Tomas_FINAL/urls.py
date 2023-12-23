"""
URL configuration for Zurita_Tomas_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Zurita_Tomas_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('lista_inscritos/', views.lista_inscritos),
    path('inscripcion/', views.inscripcion),
    path('nueva_institucion/', views.nueva_institucion),
    path('api/inscritos/', views.InscritoListCreate.as_view()),
    path('api/instituciones/', views.institucion_list),
    path('lista_instituciones/', views.lista_instituciones),
    path('eliminar_inscrito/<int:id>', views.eliminar_inscrito),
    path('modificar_inscrito/<int:id>', views.modificar_inscrito),
    path('eliminar_institucion/<int:id>', views.eliminar_institucion),
    path('modificar_institucion/<int:id>', views.modificar_institucion),
    path('datos/', views.datos)
]
