from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC, Competencia, Formacao, MakingOf, Conquista, TipoTecnologia

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'grau', 'duracao_anos')
    search_fields = ('nome', 'grau')
    list_filter = ('grau',)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'especialidade')
    search_fields = ('nome', 'especialidade')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'ects', 'ano_curricular', 'semestre', 'licenciatura')
    search_fields = ('nome', 'codigo')
    list_filter = ('ano_curricular', 'semestre', 'licenciatura')
    filter_horizontal = ('docentes',)

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel_interesse')
    search_fields = ('nome',)
    list_filter = ('categoria', 'nivel_interesse')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'unidade_curricular')
    search_fields = ('titulo', 'conceitos_aplicados')
    list_filter = ('ano', 'unidade_curricular')
    filter_horizontal = ('tecnologias',)

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano', 'classificacao', 'destaque')
    search_fields = ('titulo', 'autor')
    list_filter = ('ano', 'destaque')

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'nivel')
    search_fields = ('nome', 'categoria')
    list_filter = ('nivel', 'categoria')
    filter_horizontal = ('tecnologias', 'projetos')

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'data_inicio', 'data_fim')
    search_fields = ('titulo', 'instituicao')
    list_filter = ('instituicao',)

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('entidade_relacionada', 'data_registo')
    search_fields = ('entidade_relacionada', 'descricao')
    list_filter = ('entidade_relacionada',)

@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data')
    search_fields = ('titulo', 'tipo')
    list_filter = ('tipo',)

@admin.register(TipoTecnologia)
class TipoTecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

