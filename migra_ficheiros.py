import os
from django.core.files import File

# Escola - Curso
from escola.models import Curso
for obj in Curso.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join('media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Curso: {obj}")

# Portfolio - UnidadeCurricular
from portfolio.models import UnidadeCurricular
for obj in UnidadeCurricular.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join('media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado UnidadeCurricular: {obj}")

# Portfolio - Tecnologia
from portfolio.models import Tecnologia
for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:
        local_path = os.path.join('media', obj.logo.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.logo.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Tecnologia: {obj}")

# Portfolio - Projeto
from portfolio.models import Projeto
for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join('media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Projeto: {obj}")

# Portfolio - MakingOf
from portfolio.models import MakingOf
for obj in MakingOf.objects.all():
    if obj.foto_papel and obj.foto_papel.name:
        local_path = os.path.join('media', obj.foto_papel.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.foto_papel.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado MakingOf: {obj}")

# Artigos - Artigo
from artigos.models import Artigo
for obj in Artigo.objects.all():
    if obj.fotografia and obj.fotografia.name:
        local_path = os.path.join('media', obj.fotografia.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.fotografia.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Artigo: {obj}")

print("Migração concluída!")