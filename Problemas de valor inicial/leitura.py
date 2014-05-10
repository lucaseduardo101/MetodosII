def ler(arq):	
	a = open(arq,"r") #Abre um arquivo chamado dados.txt	
	l = []#Declara uma lista vazia que ira guardar os valores das linhas seguintes
	l.append(float ( a.readline() ) )#a primeira posicao da lista vai ser o valor de v0
	l.append(float ( a.readline() ) )#vai guardar o indice da funcao
	l.append(float ( a.readline() ) )#valor de h
	aux = []#vai guardar o intervalo
	aux = a.readline().split()
	for i in range( 0,len(aux) ):
		aux[i] = float(aux[i])		

	l.append( aux )
	
	a.close()			
	return l
