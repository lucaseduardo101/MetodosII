def ler(arq):	
	a = open(arq,"r") #Abre um arquivo chamado dados.txt	
	l = []#Declara uma lista vazia que ira guardar os valores das linhas seguintes
	l.append(int( a.readline() ) )#guarda o indice da funcao
	l.append(float(a.readline()))#guarda o valor de h
	l.append(float(a.readline()))#guarda o valor de x onde a funcao deve ser diferenciada
	
	
	a.close()			
	return l
