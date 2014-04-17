def ler():
	a = open("dados.txt","r") #Abre um arquivo chamado dados.txt
	m = int(a.readline()) #Le a primeira linha do arquivo, salva o valor dela na variavel m e a ponta para a segunda linha do arquivo
	l = []#Declara uma lista vazia que ira guardar os valores das linhas seguintes
	for i in range(0,m):
		i = a.readline() #Recebe o valor da linha seguinte em formato de String
		i = i.split(' ')# Trasforma a string em uma lista de strings em que a cada espaco em branco temos um item da lista	
		x = 0 #Variavel auxiliar que ira ajudar na etapa de transformar as strings em variaves float
		while (i[x].isdigit()): #Verifica se a proxima string da lista pode ser convertida para numeral		
			i[x] = float(i[x]) #converte a String para float
			x = x + 1	#incrementa x		
		l.append(i[0:x]) # a lista l so recebe os valores que foram convertidos	
	return l
	
print ler()
