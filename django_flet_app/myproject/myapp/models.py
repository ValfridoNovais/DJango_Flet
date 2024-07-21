# myapp/models.py
from django.db import models

class Cliente(models.Model):
    # Defina os campos de acordo com a estrutura da tabela 'cliente'
    nome = models.CharField(max_length=100)
    # Adicione outros campos aqui

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    # Defina os campos de acordo com a estrutura da tabela 'funcionarios'
    nome = models.CharField(max_length=100)
    # Adicione outros campos aqui

    def __str__(self):
        return self.nome

class Material(models.Model):
    # Defina os campos de acordo com a estrutura da tabela 'material'
    nome = models.CharField(max_length=100)
    # Adicione outros campos aqui

    def __str__(self):
        return self.nome

class Produto(models.Model):
    # Defina os campos de acordo com a estrutura da tabela 'produto'
    nome = models.CharField(max_length=100)
    # Adicione outros campos aqui

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    # Defina os campos de acordo com a estrutura da tabela 'veiculo'
    modelo = models.CharField(max_length=100)
    # Adicione outros campos aqui

    def __str__(self):
        return self.modelo
