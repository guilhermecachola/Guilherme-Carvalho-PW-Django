from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Artigo, Comentario

def artigos_view(request):
    artigos = Artigo.objects.select_related('autor').prefetch_related('comentarios', 'likes').all().order_by('-data_criacao')
    is_autor = request.user.is_authenticated and request.user.groups.filter(name='autores').exists()
    return render(request, 'artigos/artigos.html', {'artigos': artigos, 'is_autor': is_autor})
    
@login_required
def artigo_criar(request):
    if not request.user.groups.filter(name='autores').exists():
        return redirect('artigos')
    if request.method == 'POST':
        artigo = Artigo.objects.create(
            titulo=request.POST.get('titulo'),
            texto=request.POST.get('texto'),
            link_externo=request.POST.get('link_externo'),
            autor=request.user,
            fotografia=request.FILES.get('fotografia')
        )
        return redirect('artigos')
    return render(request, 'artigos/artigo_form.html')

@login_required
def artigo_editar(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect('artigos')
    if request.method == 'POST':
        artigo.titulo = request.POST.get('titulo')
        artigo.texto = request.POST.get('texto')
        artigo.link_externo = request.POST.get('link_externo')
        if request.FILES.get('fotografia'):
            artigo.fotografia = request.FILES.get('fotografia')
        artigo.save()
        return redirect('artigos')
    return render(request, 'artigos/artigo_form.html', {'artigo': artigo})

@login_required
def artigo_apagar(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if artigo.autor != request.user:
        return redirect('artigos')
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos')
    return render(request, 'artigos/artigo_confirmar_apagar.html', {'artigo': artigo})

def artigo_like(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigos')

@login_required
def comentario_criar(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.method == 'POST':
        Comentario.objects.create(
            artigo=artigo,
            autor=request.user,
            texto=request.POST.get('texto')
        )
    return redirect('artigos')