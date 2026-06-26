from django.shortcuts import render, get_object_or_404, redirect
from .models import Licenciatura, UnidadeCurricular, Tecnologia, TipoTecnologia, Projeto, TFC, Competencia, Formacao, MakingOf, Conquista
from django.contrib.auth.decorators import login_required

def index_view(request):
    return render(request, 'portfolio/landing.html')
    
def licenciatura_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciatura.html', {'licenciaturas': licenciaturas})

def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def tfcs_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias', 'projetos').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def makingof_view(request):
    makingof = MakingOf.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingof': makingof})

def conquistas_view(request):
    conquistas = Conquista.objects.all()
    return render(request, 'portfolio/conquistas.html', {'conquistas': conquistas})

@login_required
def projeto_criar(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        conceitos_aplicados = request.POST.get('conceitos_aplicados')
        url_github = request.POST.get('url_github')
        url_demo = request.POST.get('url_demo')
        video_url = request.POST.get('video_url')
        ano = request.POST.get('ano')
        uc_id = request.POST.get('unidade_curricular')
        imagem = request.FILES.get('imagem')

        uc = UnidadeCurricular.objects.get(id=uc_id) if uc_id else None
        projeto = Projeto.objects.create(
            titulo=titulo, descricao=descricao,
            conceitos_aplicados=conceitos_aplicados,
            url_github=url_github, url_demo=url_demo,
            video_url=video_url, ano=ano,
            unidade_curricular=uc, imagem=imagem
        )
        tec_ids = request.POST.getlist('tecnologias')
        projeto.tecnologias.set(tec_ids)
        return redirect('projetos')

    ucs = UnidadeCurricular.objects.all()
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/projeto_form.html', {'ucs': ucs, 'tecnologias': tecnologias})

@login_required
def projeto_editar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.titulo = request.POST.get('titulo')
        projeto.descricao = request.POST.get('descricao')
        projeto.conceitos_aplicados = request.POST.get('conceitos_aplicados')
        projeto.url_github = request.POST.get('url_github')
        projeto.url_demo = request.POST.get('url_demo')
        projeto.video_url = request.POST.get('video_url')
        projeto.ano = request.POST.get('ano')
        uc_id = request.POST.get('unidade_curricular')
        projeto.unidade_curricular = UnidadeCurricular.objects.get(id=uc_id) if uc_id else None
        if request.FILES.get('imagem'):
            projeto.imagem = request.FILES.get('imagem')
        projeto.save()
        tec_ids = request.POST.getlist('tecnologias')
        projeto.tecnologias.set(tec_ids)
        return redirect('projetos')

    ucs = UnidadeCurricular.objects.all()
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/projeto_form.html', {'projeto': projeto, 'ucs': ucs, 'tecnologias': tecnologias})

@login_required
def projeto_apagar(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projetos')
    return render(request, 'portfolio/projeto_confirmar_apagar.html', {'projeto': projeto})

# CRUD Tecnologia
@login_required
def tecnologia_criar(request):
    if request.method == 'POST':
        tec = Tecnologia.objects.create(
            nome=request.POST.get('nome'),
            categoria=request.POST.get('categoria'),
            url_oficial=request.POST.get('url_oficial'),
            descricao=request.POST.get('descricao'),
            nivel_interesse=request.POST.get('nivel_interesse'),
            logo=request.FILES.get('logo')
        )
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_form.html')

@login_required
def tecnologia_editar(request, id):
    tec = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tec.nome = request.POST.get('nome')
        tec.categoria = request.POST.get('categoria')
        tec.url_oficial = request.POST.get('url_oficial')
        tec.descricao = request.POST.get('descricao')
        tec.nivel_interesse = request.POST.get('nivel_interesse')
        if request.FILES.get('logo'):
            tec.logo = request.FILES.get('logo')
        tec.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_form.html', {'tecnologia': tec})

@login_required
def tecnologia_apagar(request, id):
    tec = get_object_or_404(Tecnologia, id=id)
    if request.method == 'POST':
        tec.delete()
        return redirect('tecnologias')
    return render(request, 'portfolio/tecnologia_confirmar_apagar.html', {'tecnologia': tec})

# CRUD Competencia
@login_required
def competencia_criar(request):
    if request.method == 'POST':
        comp = Competencia.objects.create(
            nome=request.POST.get('nome'),
            categoria=request.POST.get('categoria'),
            nivel=request.POST.get('nivel'),
            descricao=request.POST.get('descricao'),
        )
        comp.tecnologias.set(request.POST.getlist('tecnologias'))
        comp.projetos.set(request.POST.getlist('projetos'))
        return redirect('competencias')
    tecnologias = Tecnologia.objects.all()
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/competencia_form.html', {'tecnologias': tecnologias, 'projetos': projetos})

@login_required
def competencia_editar(request, id):
    comp = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        comp.nome = request.POST.get('nome')
        comp.categoria = request.POST.get('categoria')
        comp.nivel = request.POST.get('nivel')
        comp.descricao = request.POST.get('descricao')
        comp.tecnologias.set(request.POST.getlist('tecnologias'))
        comp.projetos.set(request.POST.getlist('projetos'))
        comp.save()
        return redirect('competencias')
    tecnologias = Tecnologia.objects.all()
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/competencia_form.html', {'competencia': comp, 'tecnologias': tecnologias, 'projetos': projetos})

@login_required
def competencia_apagar(request, id):
    comp = get_object_or_404(Competencia, id=id)
    if request.method == 'POST':
        comp.delete()
        return redirect('competencias')
    return render(request, 'portfolio/competencia_confirmar_apagar.html', {'competencia': comp})

# CRUD Formacao
@login_required
def formacao_criar(request):
    if request.method == 'POST':
        Formacao.objects.create(
            titulo=request.POST.get('titulo'),
            instituicao=request.POST.get('instituicao'),
            data_inicio=request.POST.get('data_inicio'),
            data_fim=request.POST.get('data_fim') or None,
            certificado_url=request.POST.get('certificado_url'),
            descricao=request.POST.get('descricao'),
        )
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_form.html')

@login_required
def formacao_editar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.titulo = request.POST.get('titulo')
        formacao.instituicao = request.POST.get('instituicao')
        formacao.data_inicio = request.POST.get('data_inicio')
        formacao.data_fim = request.POST.get('data_fim') or None
        formacao.certificado_url = request.POST.get('certificado_url')
        formacao.descricao = request.POST.get('descricao')
        formacao.save()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_form.html', {'formacao': formacao})

@login_required
def formacao_apagar(request, id):
    formacao = get_object_or_404(Formacao, id=id)
    if request.method == 'POST':
        formacao.delete()
        return redirect('formacoes')
    return render(request, 'portfolio/formacao_confirmar_apagar.html', {'formacao': formacao})

def sobre_view(request):
    tipos = TipoTecnologia.objects.prefetch_related('tecnologias').all()
    makingof = MakingOf.objects.all()
    return render(request, 'portfolio/sobre.html', {'tipos': tipos, 'makingof': makingof})

