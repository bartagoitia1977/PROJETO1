###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-10-10
#
# Descricao:  PROJETO1B - CLASSE DOCUMENTO
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

import numpy as np
from Ngrama import Ngrama

class No:
	'''
	NO VAZIO DA LISTA ENCADEADA
	'''
	def __init__(self,objeto = None,proximo = None,indice = 0):
		self._objeto = objeto
		self._proximo = proximo
		self._indice = indice

	@property
	def proximo(self):
		return self._proximo

	@proximo.setter
	def proximo(self,item):
		self._proximo = item

	@property
	def objeto(self):
		return self._objeto

	@objeto.setter
	def objeto(self,item):
		self._objeto = item

	@property
	def indice(self):
		return self._indice

	@indice.setter
	def indice(self,item):
		self._indice = item	

	def __repr__(self):
		if (type(self.objeto) == str):
			self.objetostring = "'"+str(self.objeto)+"'"
		else:
			self.objetostring = str(self.objeto)
		return self.objetostring

class LE:
	'''
	LISTA ENCADEADA SIMPLES (APENAS FUNCOES QUE SERÃO UTILIZADAS)
	'''
	def __init__(self):
		self._cabeca = self._fim = No()
		

	def anexar(self,item):
		self._item = item
		self._novono = No(self._item,None,0)
		index = 0
		aux = self._cabeca.proximo
		if (aux is None):
			self._cabeca.proximo = self._novono
			self._fim = self._novono
		else:
			while not(aux is None):
				aux = aux.proximo
				index += 1
			self._novono.indice = index
			self._fim.proximo = self._novono
			self._fim = self._novono
			
	def __str__(self):
		self._LEstring = "["
		aux = self._cabeca.proximo
		if (aux is None):
			self._LEstring = self._LEstring+"]"
			return self._LEstring
		else:
			while not(aux is None):
				self._LEstring += str(aux)+" # "
				aux = aux.proximo
			self._LEstring = self._LEstring[:-3]+"]"
			return self._LEstring

	def __repr__(self):
		return "LE(" + self.__str__() + ")"

	def __getitem__(self,item):
		self.__item = item
		finder = self._cabeca.proximo
		if (finder is None):
			raise StopIteration
		else:
			while not(finder is None) and (finder.indice != self.__item):
				finder = finder.proximo
			if (finder is None):
				raise StopIteration
			else:
				if (finder.indice == self.__item):
					return finder.objeto

	def __len__(self):
		countaux = self._cabeca.proximo
		count = 0
		while not(countaux is None):
			countaux = countaux.proximo
			count += 1
		return count
				
class Documento:
	'''
	CLASSE DOCUMENTO
	'''
	def __init__(self,documento1,documento2):
		self._documento1 = documento1
		self._documento2 = documento2
		
	def palavras1(self):
		'''
		Concentra todas as palavras do documento adotando filtro de letras minusculas e minimizando
		a poluição por caracteres alheios: espacos, pontos de interrogacao, exclamacao, etc.
		Documento1
		'''
		self._lista_de_palavras1 = np.array([])
		self._nova_palavra = True
		self._palavra = ""
		for letra in self._documento1:
			if ((letra != " ") and (letra != ".") and (letra != ",") and (letra != "\n") and (letra != ";") and
			 (letra != "?") and (letra != '"') and (letra != "(") and (letra != ")") and (letra != "[") and
			  (letra != "]") and (letra != "{") and (letra != "}") and (letra != '\'') and (letra != "*") and
			   (letra != "!") and (letra != "+") and (letra != "-") and (letra != ":") and (letra != "/")):
				if (ord(letra) >= 65) and (ord(letra) <= 90):
					self._palavra += chr(ord(letra) + 32)
					self._nova_palavra = True
				else:
					self._palavra += letra
					self._nova_palavra = True
			else:
				if (self._nova_palavra == True):
					self._lista_de_palavras1 = np.append(self._lista_de_palavras1,self._palavra)
					self._palavra = ""
					self._nova_palavra = False
		if (self._nova_palavra == True):
			self._lista_de_palavras1 = np.append(self._lista_de_palavras1,self._palavra)
			self._palavra = ""

		return self._lista_de_palavras1

	def palavras2(self):
		'''
		Concentra todas as palavras do documento adotando filtro de letras minusculas e minimizando
		a poluição por caracteres alheios: espacos, pontos de interrogacao, exclamacao, etc.
		Documento2
		'''
		self._lista_de_palavras2 = np.array([])
		self._nova_palavra = True
		self._palavra = ""
		for letra in self._documento2:
			if ((letra != " ") and (letra != ".") and (letra != ",") and (letra != "\n") and (letra != ";") and
			 (letra != "?") and (letra != '"') and (letra != "(") and (letra != ")") and (letra != "[") and
			  (letra != "]") and (letra != "{") and (letra != "}") and (letra != '\'') and (letra != "*") and
			   (letra != "!") and (letra != "+") and (letra != "-") and (letra != ":") and (letra != "/")):
				if (ord(letra) >= 65) and (ord(letra) <= 90):
					self._palavra += chr(ord(letra) + 32)
					self._nova_palavra = True
				else:
					self._palavra += letra
					self._nova_palavra = True
			else:
				if (self._nova_palavra == True):
					self._lista_de_palavras2 = np.append(self._lista_de_palavras2,self._palavra)
					self._palavra = ""
					self._nova_palavra = False
		if (self._nova_palavra == True):
			self._lista_de_palavras2 = np.append(self._lista_de_palavras2,self._palavra)
			self._palavra = ""

		return self._lista_de_palavras2

	def gerarNGramas1(self):
		'''
		Gera lista encadeada contendo todos os Ngramas (5-grama) de um dado vetor de palavras.
		Documento1
		'''
		self._lista_palavras1 = self.palavras1()
		self._lista_de_ngramas1 = LE()
		self._indice_ngrama = 0
		for ng in range(len(self._lista_palavras1) - 4):
			self._lista_de_ngramas1.anexar(Ngrama(self._lista_palavras1,self._indice_ngrama))
			self._indice_ngrama += 1
		return self._lista_de_ngramas1

	def gerarNGramas2(self):
		'''
		Gera lista encadeada contendo todos os Ngramas (5-grama) de um dado vetor de palavras.
		Documento2
		'''
		self._lista_palavras2 = self.palavras2()
		self._lista_de_ngramas2 = LE()
		self._indice_ngrama = 0
		for ng in range(len(self._lista_palavras2) - 4):
			self._lista_de_ngramas2.anexar(Ngrama(self._lista_palavras2,self._indice_ngrama))
			self._indice_ngrama += 1
		return self._lista_de_ngramas2

	def comparaNGramas(self,Ngrama_susp,Ngrama_ref):
		self._Ngrama_susp = Ngrama_susp
		self._Ngrama_ref = Ngrama_ref
		self._teste_saida = False
		self._count_string = 0
		self._count_flag = 0
		if (len(self._Ngrama_susp) != len(self._Ngrama_ref)):
			self._teste_saida = False
			return self._teste_saida
		else:
			for q in self._Ngrama_susp:
				if (q != self._Ngrama_ref[self._count_string]):
					self._count_flag += 1
				self._count_string += 1
			if (self._count_flag == 0):
				self._teste_saida = True
				return self._teste_saida
			else:
				self._teste_saida = False
				return self._teste_saida

	def contencao(self):
		self._nlista1 = self.palavras1()
		self._nlista2 = self.palavras2()
		self._N1 = len(self._nlista1)
		self._repeticoes = 0
		for ng1 in self._nlista1:
			self._flag = 0
			for ng2 in self._nlista2:
				if (self.comparaNGramas(ng1,ng2) == True):
					if (self._flag == 0):
						self._repeticoes += 1
						self._flag = 1
		self._contencao = (self._repeticoes / self._N1)
		return self._contencao