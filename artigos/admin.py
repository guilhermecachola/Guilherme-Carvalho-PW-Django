from django.contrib import admin
from .models import Artigo, Comentario

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    search_fields = ('titulo', 'autor__username')
    list_filter = ('data_criacao', 'autor')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'autor', 'data_criacao')
    search_fields = ('autor__username',)