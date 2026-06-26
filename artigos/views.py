from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Artigo, Comentario, Rating

def artigos_view(request):
    artigos = Artigo.objects.select_related('autor').prefetch_related('comentarios', 'likes', 'ratings').all().order_by('-data_criacao')
    is_autor = request.user.is_authenticated and request.user.groups.filter(name='bloggers').exists()
    return render(request, 'artigos/artigos.html', {'artigos': artigos, 'is_autor': is_autor})

@login_required
def artigo_criar(request):
    if not request.user.groups.filter(name='bloggers').exists():
        return redirect('artigos')
    if request.method == 'POST':
        Artigo.objects.create(
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
    if request.user.is_authenticated:
        if request.user in artigo.likes.all():
            artigo.likes.remove(request.user)
        else:
            artigo.likes.add(request.user)
    return redirect('artigos')

def comentario_criar(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.method == 'POST':
        texto = request.POST.get('texto')
        nome = request.POST.get('nome', 'Anónimo')
        if request.user.is_authenticated:
            Comentario.objects.create(artigo=artigo, autor=request.user, texto=texto)
        else:
            Comentario.objects.create(artigo=artigo, nome=nome, texto=texto)
    return redirect('artigos')

def rating_criar(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.method == 'POST':
        pontuacao = request.POST.get('pontuacao')
        ip = request.META.get('REMOTE_ADDR')
        Rating.objects.update_or_create(
            artigo=artigo,
            ip=ip,
            defaults={'pontuacao': pontuacao}
        )
    return redirect('artigos')