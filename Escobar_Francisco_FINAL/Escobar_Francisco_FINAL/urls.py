"""
URL configuration for Escobar_F_IEI170 project.

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
from App_Escobar_F import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('inscripciones/',views.inscripcion_list),
    path('inscripciones/<int:id>',views.inscripcion_detalle),
    path('inscrip_class/',views.inscripcion_list_class.as_view()),
    path('institucion/',views.institucion_list),
    path('institucion/<int:id>',views.institucion_detalle),
    path('institu_class/',views.institucion_list_class.as_view()),
    
    path('datos/',views.usuario),
    path('agregar/',views.agregar_instituto),
    path('agregar_inscripcion/',views.agregar_inscripcion),
    path('listar/',views.lista_inscrito),
]
