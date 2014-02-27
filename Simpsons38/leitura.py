# -*- coding: utf-8 -*-
import sys
def ler():
	arq = sys.argv[1]
	a = open(arq,"r") #Abre um arquivo chamado dados.txt
	m = int(a.readline()) #Le a primeira linha do arquivo, salva o valor dela na variavel m e a ponta para a segunda linha do arquivo
	if ( m%3 != 0 ): #verifica se m é um número multiplo de 3 
		print "O valor de m nao e um multiplo de 3 entao nao sera possivel aplicar o metodo de simpson 3/8"
		return 0
	l = []#Declara uma lista vazia que ira guardar os valores das linhas seguintes
	l.append(m)
	for i in range(0,m+1):
		i = a.readline().split() #Recebe o valor da linha seguinte em formato de String e aponta para a proxima linha se houver 
		x = 0 #Variavel auxiliar que ira ajudar na etapa de transformar as strings em variaves float
		while (x < len(i)): #Verifica se a proxima string da lista pode ser convertida para numeral		
			i[x] = float(i[x]) #converte a String para float						
			x = x + 1	#incrementa x					
		l.append(i) # a lista l so recebe os valores que foram convertidos
	a.close()			
	return l


	
	
