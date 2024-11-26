from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pessoas, name='listar_pessoas'),
    path('cadastrar/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
]
