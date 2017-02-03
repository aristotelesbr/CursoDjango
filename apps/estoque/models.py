from django.db import models
from utils.models import Cidade

class Fabricante(models.Model):
	"""docstring for Fabricante"""
	nome = models.CharField(max_length = 32, unique = True)
	endereco = models.CharField(max_length = 1024, unique = True)
	cnpj = models.CharField(max_length = 14, unique = True)
	cidade = models.ForeignKey(Cidade)

	class Meta:
		verbose_name = "Fabricante"
		verbose_name_plural = "Fabricantes"

	def __str__(self):
		return "{nome}".format(nome = self.nome)


class Categoria(models.Model):
	nome = models.CharField(max_length = 32, unique = True)

	class Meta:
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"

	def __str__(self):
		return "{n}".format(n = self.nome)


class Marca(models.Model):
	nome = models.CharField(max_length = 32, unique = True)
	fabricante = models.ForeignKey(Fabricante)

	class Meta:
		verbose_name = "Marca"
		verbose_name_plural = "Marcas"

	def __str__(self):
		return "{n}".format(n = self.nome)


class Produto(models.Model):
	nome = models.CharField(max_length = 32, unique = True)
	cod = models.CharField(max_length = 64, unique = True)
	marca = models.ForeignKey(Marca)
	categoria = models.ForeignKey(Categoria)

	class Meta:
		verbose_name = "Produto"
		verbose_name_plural = "Produtos"

	def __str__(self):
		return "{n}".format(n = self.nome)
