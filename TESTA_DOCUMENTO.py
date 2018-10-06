from Ngrama import Ngrama
from Documento import No
from Documento import LE
from Documento import Ponteiro
from Documento import Documento

texto1 = open("dados/susp/suspicious-document00442.txt","r")
suspeito = texto1.read()
texto2 = open("dados/src/source-document02777.txt","r")
referencia = texto2.read()

dados = Documento(suspeito,referencia)

vetor_palavras1 = dados.palavras1()
lista_ngramas1 = dados.gerarNGramas1()
vetor_palavras2 = dados.palavras2()
lista_ngramas2 = dados.gerarNGramas2()
	
print("\n")
print("Texto suspeito tem:",len(vetor_palavras1), "palavras.")
print("Foram gerados:",len(lista_ngramas1), "Ngramas de 5 palavras.")
print("Texto referencia tem:",len(vetor_palavras2), "palavras.")
print("Foram gerados:",len(lista_ngramas2), "Ngramas de 5 palavras.")
print("\n")
print("Aguarde...")
contencao = dados.contencao()
print("Contencao =",contencao)