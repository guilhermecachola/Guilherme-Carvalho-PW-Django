from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='portfolio_index'),
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologias/criar/', views.tecnologia_criar, name='tecnologia_criar'),
    path('tecnologias/<int:id>/editar/', views.tecnologia_editar, name='tecnologia_editar'),
    path('tecnologias/<int:id>/apagar/', views.tecnologia_apagar, name='tecnologia_apagar'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('projetos/criar/', views.projeto_criar, name='projeto_criar'),
    path('projetos/<int:id>/editar/', views.projeto_editar, name='projeto_editar'),
    path('projetos/<int:id>/apagar/', views.projeto_apagar, name='projeto_apagar'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencias/criar/', views.competencia_criar, name='competencia_criar'),
    path('competencias/<int:id>/editar/', views.competencia_editar, name='competencia_editar'),
    path('competencias/<int:id>/apagar/', views.competencia_apagar, name='competencia_apagar'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacoes/criar/', views.formacao_criar, name='formacao_criar'),
    path('formacoes/<int:id>/editar/', views.formacao_editar, name='formacao_editar'),
    path('formacoes/<int:id>/apagar/', views.formacao_apagar, name='formacao_apagar'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('conquistas/', views.conquistas_view, name='conquistas'),
    path('sobre/', views.sobre_view, name='sobre'),
]