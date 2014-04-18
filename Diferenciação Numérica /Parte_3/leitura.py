# -*- coding: utf-8 -*-
def ler(arq):	
	a = open(arq,"r") #Abre um arquivo 
	m = a.readline().split() #Le a primeira linha do arquivo, salva o valor dela na variavel m e a ponta para a segunda linha do arquivo
	m = int (m[0])
			
	l = []#Declara uma lista vazia que ira guardar os valores das linhas seguintes
	l.append(m)
	
	for i in range(0, m + 1):
		i = a.readline().split() #Recebe o valor da linha seguinte em formato de String e aponta para a proxima linha se houver 
		x = 0 #Variavel auxiliar que ira ajudar na etapa de transformar as strings em variaves float
		while (x < len(i)): #Verifica se a proxima string da lista pode ser convertida para numeral		
			i[x] = float(i[x]) #converte a String para float						
			x = x + 1	#incrementa x					
		l.append(i) # a lista l so recebe os valores que foram convertidos
	
	print l
	a.close()			
	return l
	
ler("entrada.txt")

	
	
