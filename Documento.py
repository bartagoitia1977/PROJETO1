
import numpy as np

class No:
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
	def __init__(self):
		self._cabeca = self._fim = No()
		self._aux = self._cabeca.proximo
		
	def anexar(self,item):
		self._item = item
		self._novono = No(self._item,None,0)
		index = 0
		aux = self._cabeca.proximo
		while not(aux is None):
			aux = aux.proximo
			index += 1
		if (aux is None):
			self._fim.proximo = self._novono
			self._fim = self._novono
			self._fim.indice = index

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
			raise KeyError
		else:
			while not(finder is None) and (finder.indice != self.__item):
				finder = finder.proximo
			if (finder is None):
				raise KeyError
			else:
				if (finder.indice == self.__item):
					return finder.objeto

	def __iter__(self):
		if not (self._aux is None):
			return self._aux.objeto
		else:
			raise StopIteration

	def __next__(self):
		if not (self._aux is None):
			self._aux = self._aux.proximo
		else:
			raise StopIteration
				
class Documento:
	
	def __init__(self,documento):
		self._documento = documento
		
	def cata_palavra(self):
		self._lista_de_palavras = np.array([])
		self._nova_palavra = True
		self._palavra = ""
		for letra in self._documento:
			if ((letra != " ") and (letra != ".") and (letra != ",") and (letra != "\n") and (letra != ";") and
			 (letra != "?") and (letra != '"') and (letra != "(") and (letra != ")") and (letra != "[") and
			  (letra != "]") and (letra != "{") and (letra != "}") and (letra != "!")):
				if (ord(letra) >= 65) and (ord(letra) <= 90):
					self._palavra += chr(ord(letra) + 32)
					self._nova_palavra = True
				else:
					self._palavra += letra
					self._nova_palavra = True
			else:
				if (self._nova_palavra == True):
					self._lista_de_palavras = np.append(self._lista_de_palavras,self._palavra)
					self._palavra = ""
					self._nova_palavra = False
		if (self._nova_palavra == True):
			self._lista_de_palavras = np.append(self._lista_de_palavras,self._palavra)
			self._palavra = ""

		return self._lista_de_palavras


		


	



