from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_view, name='artigos'),
    path('criar/', views.artigo_criar, name='artigo_criar'),
    path('<int:id>/editar/', views.artigo_editar, name='artigo_editar'),
    path('<int:id>/apagar/', views.artigo_apagar, name='artigo_apagar'),
    path('<int:id>/like/', views.artigo_like, name='artigo_like'),
    path('<int:artigo_id>/comentario/', views.comentario_criar, name='comentario_criar'),
]