# -*- coding: utf-8 -*-
def ler():
	a = open("dados.txt","r") #Abre um arquivo chamado dados.txt
	m = int(a.readline()) #Le a primeira linha do arquivo, salva o valor dela na variavel m e a ponta para a segunda linha do arquivo
	c = [] #lista dos coeficientes
	if ( m%3 != 0 ): #verifica se m é um número multiplo de 3 
		print "O valor de m nao e um multiplo de 3 entao nao sera possivel aplicar o metodo de simpson 3/8"
		return 0
	l = []#Declara uma lista vazia que ira guardar os valores das linhas seguintes
	for i in range(0,m):
		caux = i #auxiliar para calcular os coeficientes... depois melhorar isso... 
		i = a.readline() #Recebe o valor da linha seguinte em formato de String e aponta para a proxima linha se houver 
		i = i.split(' ')# Trasforma a string em uma lista de strings em que a cada espaco em branco temos um item da lista	
		x = 0 #Variavel auxiliar que ira ajudar na etapa de transformar as strings em variaves float
		while (i[x].isdigit()): #Verifica se a proxima string da lista pode ser convertida para numeral		
			i[x] = float(i[x]) #converte a String para float						
			x = x + 1	#incrementa x					
		l.append(i[0:x]) # a lista l so recebe os valores que foram convertidos
		if ( caux == 0 or caux == m-1): 
			c.append(0)
		elif ( caux%3 == 0):
			c.append(2)
		else:
			c.append(3)
	l.append((l[0][0] + l[1][1])/2) #cálculo de H, melhorar isso depois...
	l.append(c)
	return l
	