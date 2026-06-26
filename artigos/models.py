from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotografia = models.ImageField(upload_to='artigos/', blank=True)
    link_externo = models.URLField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos')
    likes = models.ManyToManyField(User, blank=True, related_name='artigos_gostados')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comentarios')
    nome = models.CharField(max_length=100, blank=True)  # para não autenticados
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário em {self.artigo}"
    def __str__(self):
        return f"Comentário de {self.autor} em {self.artigo}"

class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='ratings')
    pontuacao = models.IntegerField()  # 1 a 5
    ip = models.GenericIPAddressField()  

    def __str__(self):
        return f"Rating {self.pontuacao} em {self.artigo}"