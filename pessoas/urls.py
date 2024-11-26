from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('listar/', views.listar_pessoas, name='listar_pessoas'),
    path('cadastrar/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('deletar/<int:pessoa_id>/', views.deletar_pessoa, name='deletar_pessoa'),
    path('editar/<int:pessoa_id>/', views.editar_pessoa, name='editar_pessoa'),
]