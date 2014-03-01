def ler():
	a = open("dados.txt","r") #Abre um arquivo chamado dados.txt
	m = int(a.readline()) #Le a primeira linha do arquivo, salva o valor dela na variavel m e a ponta para a segunda linha do arquivo
	l = []
	l.append(m)
	for i in range(0,m+1):
		i = a.readline().split() #Recebe o valor da linha seguinte em formato de String e aponta para a proxima linha se houver
		x = 0 #Variavel auxiliar que ira ajudar na etapa de transformar as strings em variaves float
		while (x < len(i)): #Verifica se a proxima string da lista pode ser convertida para numeral
			i[x] = float(i[x]) #converte a String para float
			x = x + 1	#incrementa x
		l.append(i) # a lista l so recebe os valores que foram convertidos
	return l	
print ler()	

