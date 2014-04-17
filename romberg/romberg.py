#!/usr/bin/python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------------------
# Descrição: Implementacao para integracao numerica utilizando o metodo de Romberg.
#			 Para executa-lo, abra o terminal ou cmd(Windows),
#			 entre no diretório onde se encontra o arquivo 'romberg.py', e 
#			 digite -> python romberg.py nomeDoArquivo.txt
# Valores no arquivo:
# Primeira linha: h1-> o valor de h1. (h2 sera h1/2).
# segunda linha: f(x)-> valor de identificacao a funcao na tabela dada abaixo.
#
# 			-----------------------------------------
#			|	indices	|			funcao			|	
#			-----------------------------------------		
#			| 	  1  	|	   	   1/sqrt(x)		|
#			| 	  2  	|	     1/sqrt(1-x^2)		|
#			| 	  3 	|   2x^3 + 3x^2 + 6x + 1	|
#			| 	  4  	|	1 - x -4x^3 + 2x^5		|
#			| 	  5  	|	      4/(1 + x^2)		|
#			-----------------------------------------

# terceira linha: a b - > valores dos intervalos de integracao.

# Saída: resultado da integral f(x) no intervalo [a,b].

# Aluno: 	 Ricardo Sousa
# 
#-----------------------------------------------------------------------------------------------------------

import sys
from math import sqrt, exp, sin, cos


def selecionaFunc(indice):
	
	if (indice == 1):
		return lambda x: 1/sqrt(x)
	elif (indice == 2):
		return lambda x: 1/sqrt(1-x**2)
	elif (indice == 3):
		return lambda x: 2 * x**3 + 3 * x**2 + 6 * x + 1	
	elif (indice == 4):
		return lambda x: 1 - x -4 * x**3 + 2 * x **5	
	elif (indice == 5):
		return lambda x: 4/(1 + x**2)
	else:
		print ('Funcao nao definida na tabela.')
		exit()
		
def trapezio(f, a, b, n=10000):

    h = float(b - a) / n
    sumatory = sum([f(a + i * h) for i in xrange(1, n)])
    trapezoids = f(a) + 2.0 * sumatory + f(a + n * h)
    integral = trapezoids * (h / 2.0)
    return integral

def rombergMetodo(f, a, b, n=20):
	try:
		def calculatrapezio(s, k, i):
			m = 2 ** (k - 1)
			si = trapezio(f, a, b, m)
			return (s[i], si)

		def melhorar_conv(s, var, i, k):
			sk = (4 ** (i - 1) * s[i - 1] - var) / (4 ** (i - 1) - 1)
			return (sk, s[i], s[k])

		def calcular():
			var = 0.0
			s = [1.0 for i in xrange(0, n)]
			for k in xrange(1, n):
				for i in xrange(1, k + 1):
					if i == 1:
						(var, s[i]) = calculatrapezio(s, k, i)
					else:
						(s[k], var, s[i]) = melhorar_conv(s, var, i, k)
			return s[n - 1]

		return calcular()
	except:
		print('Erro de divisao por zero.')
		print('Tente um intervalo compativel com o da funcao.')
		exit()


def lerArquivo(nomeArquivo):
	try:
		arq = open(nomeArquivo)
	except:
		print (u'Erro. Arquivo Nao Encontrado.')
		exit()
		
	try:
		valores = [0, 0, 0, 0]
		i = 0
		a = 0
		for line in arq:
			if (i != 2):
				valores[i] = int(line)
			else:
				valAuxs = line.split()
				k = len(valAuxs)
				while (a < 2 or a < k):
					valores[i] = float(valAuxs[a])
					a += 1
					i += 1	#incremento dentro do while. Nao remover.
			i +=1 #incremento dentro do for. Nao remover.
			
	except:
		print (u'Erro. Dados incompativeis. Tente rever a forma dos dados no arquivo.')
		exit()
		
	arq.close()		
	return valores
	
if __name__ == "__main__":
	
	try:
		nomeArquivo = sys.argv[1]
	except:
		print ("Ao executar o codigo digite o nome do arquivo para leitura.")
	
	valores = lerArquivo(nomeArquivo)
	#atribuicao de valores
	if (valores[0] % 2 == 0):
		h1 = valores[0]
	else:
		print (u'Erro. Verifique o valor de h1 (Deve pertence ao conjunto: {2,4,6,...})')
		exit()
	
	numf = valores[1]
	a = valores[2]
	b = valores[3]
	
	#Chama a funcao que seleciona a funcao a ser integrada, conforme a tabela.
	f = selecionaFunc(numf)
	#Chama a funcao que calcular a integral da funcao escolhida.
	solucao= rombergMetodo(f, a, b, h1)
	#Mostra o valor.
	print "Valor numerico da integral: %8f"%(solucao)
