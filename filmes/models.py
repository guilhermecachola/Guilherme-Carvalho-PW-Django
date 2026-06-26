from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Realizador(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.IntegerField()
    sinopse = models.TextField()
    duracao = models.IntegerField()  # em minutos
    classificacao = models.FloatField()  # 0 a 10
    poster = models.ImageField(upload_to='filmes/', blank=True)
    realizador = models.ForeignKey(Realizador, on_delete=models.SET_NULL, null=True, related_name='filmes')
    generos = models.ManyToManyField(Genero, blank=True, related_name='filmes')

    def __str__(self):
        return self.titulo