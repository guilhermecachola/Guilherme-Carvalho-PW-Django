from django.contrib import admin
from .models import Filme, Realizador, Genero

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Realizador)
class RealizadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'data_nascimento')
    search_fields = ('nome', 'nacionalidade')

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'realizador', 'classificacao')
    search_fields = ('titulo',)
    list_filter = ('ano', 'generos', 'realizador')
    filter_horizontal = ('generos',)