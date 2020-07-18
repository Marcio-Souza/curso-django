from django.urls import path

from pypro.modulos.views import detalhe, aula

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', detalhe, name='detalhe'),
    path('/aula/<slug:slug>', aula, name='aula'),
]
