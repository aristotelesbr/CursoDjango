from django.db import models

# Create your models here.
class Regiao(models.Model):
	# Validação de unicidade
	nome = models.CharField(max_length = 32, unique = True)
	sigla = models.CharField(max_length = 2, unique = True)

	class Meta:
		verbose_name = "Região"
		verbose_name_plural = "Regiões"

	def __str__(self):
		return "{n}({s})".format(n = self.nome, s = self.sigla)


class Estado(models.Model):
	"""docstring for Estado"""
	nome = models.CharField(max_length = 32, unique = True)
	sigla = models.CharField(max_length = 2, unique = True)
	regiao = models.ForeignKey(Regiao)

	def __str__(self):
		return "{n}".format(n = self.nome)


class Cidade(models.Model):
	"""docstring for Cidade"""
	nome = models.CharField(max_length = 32, unique = True)
	stado = models.ForeignKey(Estado)
	ddd = models.CharField(max_length = 2)

	def __str__(self):
		return "{n}".format(n = self.nome)
