"""
URL configuration for Sistema_optimizacion_PG project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Modulo2.views import ChatbotAPI
from formularios.views import SolicitudVisaAPIView, SolicitudPasaporteAPIView, SolicitudCedulaAPIView,TramiteAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ChatbotAPI/', ChatbotAPI.as_view(), name='ChatbotAPI'),
    path('solicitar-visa/', SolicitudVisaAPIView.as_view(), name='solicitar_visa_api'),
    path('solicitar-visa/<int:id>/', SolicitudVisaAPIView.as_view(), name='solicitar_visa_api_detail'),
    path('solicitar-pasaporte/', SolicitudPasaporteAPIView.as_view(), name='solicitar_pasaporte_api'),
     path('solicitar-pasaporte/<int:id>/', SolicitudPasaporteAPIView.as_view(), name='solicitar_pasaporte_api_detail'),
    path('solicitar-cedula/', SolicitudCedulaAPIView.as_view(), name='solicitar_cedula_api'),
    path('solicitar-cedula/<int:id>/', SolicitudCedulaAPIView.as_view(), name='solicitar_cedula_api_detail'),
    path('tramite/<int:id>/', TramiteAPIView.as_view(), name='solicitar_tramite_id'),
    path('tramite/', TramiteAPIView.as_view(), name='solicitar_tramite'),

]
