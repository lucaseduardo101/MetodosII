# -*- coding: utf-8 -*-
def ler(arq):	
	a = open(arq,"r") #Abre um arquivo chamado dados.txt	
	l = []#Declara uma lista vazia que ira guardar os valores das linhas seguintes
	l.append(float ( a.readline() ) )#a primeira posicao da lista vai ser o valor de n
	l.append(float ( a.readline() ) )
	aux = []
	aux = a.readline().split()
	for i in range( 0,len(aux) ):
		aux[i] = float(aux[i])		

	l.append( aux )
	
	a.close()			
	return l

