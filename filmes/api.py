from ninja import NinjaAPI
from typing import List, Optional
from django.shortcuts import get_object_or_404
from .models import Filme, Realizador, Genero
from .schemas import FilmeIn, FilmeOut, RealizadorIn, RealizadorOut, GeneroOut, ErrorSchema

api = NinjaAPI(
    title="API RESTful de Filmes",
    description="API para gerir filmes com operações CRUD completas",
    version="1.0.0"
)

# ── FILMES ────────────────────────────────────────────

@api.get("filmes/", response={200: List[FilmeOut]}, tags=["Filmes"],
         description="Lista todos os filmes")
def list_filmes(request, titulo: str = None, ano: int = None,
                limit: int = 10, offset: int = 0):
    filmes = Filme.objects.select_related('realizador').prefetch_related('generos').all()
    if titulo:
        filmes = filmes.filter(titulo__icontains=titulo)
    if ano:
        filmes = filmes.filter(ano=ano)
    return 200, filmes[offset:offset+limit]

@api.get("filmes/{filme_id}/", response={200: FilmeOut, 404: ErrorSchema},
         tags=["Filmes"], description="Obtém um filme pelo ID")
def get_filme(request, filme_id: int):
    return 200, get_object_or_404(
        Filme.objects.select_related('realizador').prefetch_related('generos'),
        id=filme_id
    )

@api.post("filmes/", response={201: FilmeOut, 400: ErrorSchema},
          tags=["Filmes"], description="Cria um novo filme")
def post_filme(request, data: FilmeIn):
    filme = Filme.objects.create(**data.dict())
    return 201, filme

@api.put("filmes/{filme_id}/", response={200: FilmeOut, 404: ErrorSchema},
         tags=["Filmes"], description="Atualiza um filme")
def put_filme(request, filme_id: int, data: FilmeIn):
    filme = get_object_or_404(Filme, id=filme_id)
    for attr, value in data.dict().items():
        setattr(filme, attr, value)
    filme.save()
    return 200, filme

@api.delete("filmes/{filme_id}/", response={204: None, 404: ErrorSchema},
            tags=["Filmes"], description="Apaga um filme")
def delete_filme(request, filme_id: int):
    filme = get_object_or_404(Filme, id=filme_id)
    filme.delete()
    return 204, None

# ── REALIZADORES ──────────────────────────────────────

@api.get("realizadores/", response={200: List[RealizadorOut]}, tags=["Realizadores"],
         description="Lista todos os realizadores")
def list_realizadores(request, nome: str = None, limit: int = 10, offset: int = 0):
    realizadores = Realizador.objects.all()
    if nome:
        realizadores = realizadores.filter(nome__icontains=nome)
    return 200, realizadores[offset:offset+limit]

@api.get("realizadores/{real_id}/", response={200: RealizadorOut, 404: ErrorSchema},
         tags=["Realizadores"], description="Obtém um realizador pelo ID")
def get_realizador(request, real_id: int):
    return 200, get_object_or_404(Realizador, id=real_id)

@api.post("realizadores/", response={201: RealizadorOut, 400: ErrorSchema},
          tags=["Realizadores"], description="Cria um novo realizador")
def post_realizador(request, data: RealizadorIn):
    return 201, Realizador.objects.create(**data.dict())

@api.put("realizadores/{real_id}/", response={200: RealizadorOut, 404: ErrorSchema},
         tags=["Realizadores"], description="Atualiza um realizador")
def put_realizador(request, real_id: int, data: RealizadorIn):
    realizador = get_object_or_404(Realizador, id=real_id)
    for attr, value in data.dict().items():
        setattr(realizador, attr, value)
    realizador.save()
    return 200, realizador

@api.delete("realizadores/{real_id}/", response={204: None, 404: ErrorSchema},
            tags=["Realizadores"], description="Apaga um realizador")
def delete_realizador(request, real_id: int):
    realizador = get_object_or_404(Realizador, id=real_id)
    realizador.delete()
    return 204, None

# ── GENEROS ───────────────────────────────────────────

@api.get("generos/", response={200: List[GeneroOut]}, tags=["Generos"],
         description="Lista todos os géneros")
def list_generos(request):
    return 200, Genero.objects.all()

@api.get("generos/{genero_id}/", response={200: GeneroOut, 404: ErrorSchema},
         tags=["Generos"], description="Obtém um género pelo ID")
def get_genero(request, genero_id: int):
    return 200, get_object_or_404(Genero, id=genero_id)