###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-10-14
#
# Descricao:  PROJETO1B - CLASSE CORPUS
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

import numpy as np
from Ngrama import Ngrama
from Documento import No
from Documento import LE
from Documento import Ponteiro
from Documento import Documento

class Corpus:
	'''
	Recebe lista de documentos referencia a serem analisados.
	Dentro da lista como parametro: ["filename1.txt","filename2.txt",...]
	'''

	def __init__(self,lista_de_referencias):
		self._lista_de_referencias = lista_de_referencias
		self._dicref = {}
		for file in self._lista_de_referencias:
			self._ref = open(file,"r")
			self._ref_dados = self._ref.read()
			self._dicref[file] = self._ref_dados
		
	def VerificarPlagio(self,doc_suspeito,limiar):
		'''
		Pega um documento suspeito de plagio e analisa atraves de um limiar.
		Retorna lista de bases para o plagio ordenada em ordem crescente: primeiro arquivo menor contencao
		ultimo arquivo maior contencao.
		Parametro doc_suspeito "filename.txt"
		Limiar numero entre 0 e 1 (float)
		'''
		self._doc_suspeito = doc_suspeito
		self._limiar = limiar
		self._dic_acima_do_limiar = {}
		self._susp = open(self._doc_suspeito,"r")
		self._susp_dados = self._susp.read()
		self._listacontencao = []
		self._saida = []
		print("Arquivo suspeito:",self._doc_suspeito)
		for filename in self._dicref:
			self._dados = Documento(self._susp_dados,self._dicref[filename])
			print("Testando o arquivo:",filename)
			self._contencao = self._dados.contencao()
			if (self._contencao >= self._limiar):
				self._dic_acima_do_limiar[str(self._contencao)] = filename
		for cont in self._dic_acima_do_limiar:
			self._listacontencao.append(cont)

		self._listacontencaoord = self.ordenar(self._listacontencao)
		for valor in self._listacontencaoord:
			self._saida.append(self._dic_acima_do_limiar[valor])
		return self._saida
		
	def trocar(self,lista,A,B):
		'''
		Trocar do Bubblesort
		'''
		self._lista = lista
		self._A = A
		self._B = B
		self._aux = self._lista[self._A]
		self._lista[self._A] = self._lista[self._B]
		self._lista[self._B] = self._aux

	def ordenar(self,lista):
		'''
		Bubblesort
		'''
		self._lista = lista
		self._tamanho = len(self._lista)
		for e in range((self._tamanho - 1),0,-1):
			for f in range(0,e):
				if float(self._lista[f]) > float(self._lista[f + 1]):
					self.trocar(self._lista,f,f + 1)
		return self._lista