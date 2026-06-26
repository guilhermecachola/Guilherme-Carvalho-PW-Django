from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    grau = models.CharField(max_length=50)
    duracao_anos = models.IntegerField()
    url_oficial = models.URLField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    url_lusofona = models.URLField()
    especialidade = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20)
    ects = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ano_curricular = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='ucs/', blank=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')
    docentes = models.ManyToManyField(Docente, blank=True)

    def __str__(self):
        return self.nome

class TipoTecnologia(models.Model):
    nome = models.CharField(max_length=100)  # ex: "Frontend", "Backend", "Base de Dados"

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    CATEGORIAS = [
        ('linguagem', 'Linguagem'),
        ('framework', 'Framework'),
        ('ferramenta', 'Ferramenta'),
        ('base_dados', 'Base de Dados'),
    ]
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    logo = models.ImageField(upload_to='tecnologias/', blank=True)
    url_oficial = models.URLField()
    descricao = models.TextField()
    nivel_interesse = models.IntegerField(default=3)
    tipo = models.ForeignKey(TipoTecnologia, on_delete=models.SET_NULL, null=True, blank=True, related_name='tecnologias')

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    url_github = models.URLField()
    url_demo = models.URLField(blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True)
    video_url = models.URLField(blank=True)
    ano = models.IntegerField()
    unidade_curricular = models.ForeignKey(
        UnidadeCurricular, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='projetos'
    )
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.titulo

class TFC(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=200)
    resumo = models.TextField()
    ano = models.IntegerField()
    classificacao = models.IntegerField()  # 0 a 20
    url_documento = models.URLField(blank=True)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)  
    descricao = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    projetos = models.ManyToManyField(Projeto, blank=True)

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    titulo = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    certificado_url = models.URLField(blank=True)
    descricao = models.TextField(blank=True)

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return self.titulo

class MakingOf(models.Model):
    entidade_relacionada = models.CharField(max_length=100)
    descricao = models.TextField()
    decisoes = models.TextField(blank=True)
    erros_correcoes = models.TextField(blank=True)
    uso_ia = models.TextField(blank=True)
    foto_papel = models.ImageField(upload_to='makingof/', blank=True)
    data_registo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MakingOf - {self.entidade_relacionada}"

class Conquista(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    tipo = models.CharField(max_length=100)  
    url_evidencia = models.URLField(blank=True)

    def __str__(self):
        return self.titulo