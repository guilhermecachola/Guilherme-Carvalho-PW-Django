from ninja import Schema
from typing import List, Optional

class ErrorSchema(Schema):
    detail: str

class GeneroOut(Schema):
    id: int
    nome: str

class RealizadorIn(Schema):
    nome: str
    nacionalidade: str
    data_nascimento: Optional[str] = None

class RealizadorOut(RealizadorIn):
    id: int

class FilmeIn(Schema):
    titulo: str
    ano: int
    sinopse: str
    duracao: int
    classificacao: float

class FilmeOut(Schema):
    id: int
    titulo: str
    ano: int
    sinopse: str
    duracao: int
    classificacao: float
    realizador: Optional[RealizadorOut] = None
    generos: List[GeneroOut] = []

    @staticmethod
    def resolve_generos(obj):
        return obj.generos.all()