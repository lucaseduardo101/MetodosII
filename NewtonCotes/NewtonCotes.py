# -*- coding: utf-8 -*-
import sys
import leitura
from math import sqrt, exp, sin, cos

arq = sys.argv[1]
l = leitura.ler(arq)
#falta receber esses valores do arquivo txt

n=l[0]#recebe o valor de n
i=l[1]#recebe o numero da funcao escolhida
a=l[2][0] #recebe o limite inferior
b=l[2][1] #recebe o limite superior

# Escolha da funcao
# 			-----------------------------------------
#			|	indices	|			#			|	
#			-----------------------------------------		
#			| 	  1  	|	   	   1/sqrt(x)		|
#			| 	  2  	|	     1/sqrt(1-x^2)		|
#			| 	  3 	|   2x^3 + 3x^2 + 6x + 1	|
#			| 	  4  	|	1 - x -4x^3 + 2x^5		|
#			| 	  5  	|	      4/(1 + x^2)		|
#			-----------------------------------------

print "funcao numero:",i

#selecionaFunc(funcao)
def f(indice,x):	
	if (indice == 0):
		return (2*x**3 + 3*x**2 + 6*x+1)
	if (indice == 1):
		return (1/sqrt(x))
	elif (indice == 2):
		return (1/sqrt(1-x**2))
	elif (indice == 3):
		return (2 * x**3 + 3 * x**2 + 6 * x + 1)
	elif (indice == 4):
		return (1 - x -4 * x**3 + 2 * x **5)	
	elif (indice == 5):
		return (4/(1 + x**2))
	else:
		print ('Funcao nao definida na tabela.')
		exit()


#Newton Cotes fechada de grau = 1
def newtonCotesFechadaGrau1():
	
	return (b-a)*(f(i,a) + f(i,b))/2 

print "valor calculado obtido pela fórmula Newton Cotes fechada de grau 1: ",newtonCotesFechadaGrau1()


#Newton Cotes fechada de grau = 2
def newtonCotesFechadaGrau2():
	
	return (b-a)*(f(i,a) + (4*f(i,(a+b)/2)) + f(i,b))/6

print "valor calculado obtido pela fórmula Newton Cotes fechada de grau 2: ",newtonCotesFechadaGrau2()


#Newton Cotes fechada de grau = 3
def newtonCotesFechadaGrau3():
	
	return (b-a)*(f(i,a) + (3*f(i,(2*a+b)/3)) + (3*f(i,(a+2*b)/3)) + f(i,b))/8

print "valor calculado obtido pela fórmula Newton Cotes fechada de grau 3: ",newtonCotesFechadaGrau3()


#Newton Cotes fechada de grau = 4
def newtonCotesFechadaGrau4():
	
	return (b-a)*(f(i,a) + (32*f(i,(3*a+b)/4)) + (12*f(i,(a+b)/2)) + (32*f(i,(a+3*b)/4)) +    f(i,b))/90

print "valor calculado obtido pela fórmula Newton Cotes fechada de grau 4: ",newtonCotesFechadaGrau4()


#Newton Cotes aberta de grau = 1
def newtonCotesAbertaGrau1():
	
        aux=(b-a)/3;
        return (b-a)*(f(i,a+aux) + f(i,a+(2*aux)))/2;

print "valor calculado obtido pela fórmula Newton Cotes aberta de grau 1: ",newtonCotesAbertaGrau1()


#Newton Cotes aberta de grau = 2
def newtonCotesAbertaGrau2():
	
	h=(b-a)/4;
	return (b-a)*(2*f(i,a+h) - f(i,a+2*h) + 2*f(i,a+3*h))/3;

print "valor calculado obtido pela fórmula Newton Cotes aberta de grau 2: ",newtonCotesAbertaGrau2()


#Newton Cotes aberta de grau = 3
def newtonCotesAbertaGrau3():
	
	h=(b-a)/5;
	return (b-a)*(11*f(i,a+h) + f(i,a+2*h) + f(i,a+3*h)+ 11*f(i,a+4*h))/24;

print "valor calculado obtido pela fórmula Newton Cotes aberta de grau 3: ",newtonCotesAbertaGrau3()


#Newton Cotes aberta de grau = 4
def newtonCotesAbertaGrau4():
	
	h=(b-a)/6;
	return (b-a)*(11*f(i,a+h) - 14*f(i,a+2*h) + 26*f(i,a+3*h) - 14*f(i,a+4*h) + 11*f(i,a+5*h))/20

print "valor calculado obtido pela fórmula Newton Cotes aberta de grau 4: ",newtonCotesAbertaGrau4()

