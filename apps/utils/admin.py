from django.contrib import admin
from . models import Regiao, Estado, Cidade

# INLINES
# TabularInline -> Muda a tabulação na exibição da lista
# StackedInline -> Muda a tabulação na exibição da lista
class EstadoInline(admin.TabularInline):
	model = Estado
	# Remove os campos adicionais criado com nestendForm
	extra = 0


class CidadeInline(admin.StackedInline):
	model = Cidade
	# Remove os campos adicionais criado com nestendForm
	extra = 0


# MODEL ADMIN
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'sigla', 'regiao')
	list_filter = ('regiao',)
	inlines = [
		CidadeInline,
		]


class RegiaoAdmin(admin.ModelAdmin):
	# Formata as tabelas de exibição.
	list_display = ('nome', 'sigla')
	# Gera o nestendForm
	inlines = [
		EstadoInline,
		]


admin.site.register(Regiao, RegiaoAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade)
