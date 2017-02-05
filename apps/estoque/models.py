from django.db import models
from utils.models import Cidade

class Fabricante(models.Model):
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
	codigo = models.CharField(max_length = 64, unique = True)
	marca = models.ForeignKey(Marca)
	categoria = models.ForeignKey(Categoria)

	class Meta:
		verbose_name = "Produto"
		verbose_name_plural = "Produtos"

	def __str__(self):
		return "{n}".format(n = self.nome)


class Lote(models.Model):
		codigo = models.CharField(max_length = 16, unique = True)
		produto = models.ForeignKey(Produto)
		data_validade = models.DateField()

		class Meta:
			verbose_name = "Lote"
			verbose_name_plural = "Lotes"

		def __str__(self):
			return "[{c}]p".format(p = self.produto, c = self.codigo)


class Prateleira(models.Model):
		codigo = models.CharField(max_length = 16)
		categoria = models.ForeignKey(Categoria)

		class Meta:
			verbose_name = "Prateleira"
			verbose_name_plural = "Prateleiras"

		def __str__(self):
			return "[{c}]cat".format(cat = self.categoria, c = self.codigo)


class Estoque(models.Model):
		lote = models.ForeignKey(Lote)
		quantidade = models.DecimalField(max_digits = 5, decimal_places = 2)
		prateleira = models.ForeignKey(Prateleira)

		class Meta:
			unique_together = ('lote', 'prateleira')
			verbose_name = "Estoque"
			verbose_name_plural = "Estoque de Produtos"

		def __str__(self):
			return "[{c}]:{l}".format(l = self.lote, c = self.codig)