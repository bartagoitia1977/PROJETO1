from Corpus import Corpus
import os
listaref = []
list_ref = os.listdir("dados/src")
for filename in list_ref:
	listaref.append("dados/src/" + filename)

listasusp = []
list_susp = os.listdir("dados/susp")
for file in list_susp:
	listasusp.append("dados/susp/" + file)

work = Corpus(listaref)

for arqsuspeito in listasusp:
	a = work.VerificarPlagio(arqsuspeito,0.01)
	print(a)
