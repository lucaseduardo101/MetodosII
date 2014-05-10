import numpy


class MatrizUtil:
	
	m = numpy.empty
	ordem = 0 
	e = float("inf")
	
	
	def lerArquivo(self, arq): #Cria uma matriz com as especificacoes do arquivo 
		a = open(arq,"r") #Abre um arquivo chamado dados.txt
		self.ordem = int(a.readline()) #Le a primeira linha do arquivo, que sera a ordem da matriz
		l = numpy.empty([self.ordem,self.ordem])
		
		for i in range(0,self.ordem):
			r = i			
			i = a.readline().split() #Recebe o valor da linha seguinte em formato de String e aponta para a proxima linha se houver
			x = 0 #Variavel auxiliar que ira ajudar na etapa de transformar as strings em variaves float
			while (x < len(i)): #Verifica se a proxima string da lista pode ser convertida para numeral
				i[x] = float(i[x]) #converte a String para float
				x = x + 1	#incrementa x
			j = numpy.array(i)
			l[r] = j # a lista l so recebe os valores que foram convertidos
		e = float(a.readline())
		self.m = l
		
	def potencia():
		q0  = numpy.identity(ordem)
		zk	= []
		zk.append(m*q0)
		v, vk = 0		
		
		while ( (vk - v) <=  e ):			
			soma = numpy.empty(self.ordem, self.ordem)
			for i in zK:
				soma = soma + i 
			qk = 
						
		

