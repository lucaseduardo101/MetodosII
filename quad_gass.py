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


#selecionaFunc(funcao)

#funcao que calcula o x apos a mudanca de variavel
def x(t):
	return ((b-a)/2)*t + (a+b)/2

#Quadratura gaussiana para n=2
def quadGaussiana2():
	#valores da tabela para mudanca de variavel para n=2
	t1=-0.5774
	t2=0.5774
	A0=1
	A1=1

	#calculo dos valores de x
	x1=x(t1)
	x2=x(t2)
	return ((b-a)/2) * (A0*f(i,x1)+A1*f(i,x2))

print "valor da Quandratura para n=2 =>",quadGaussiana2()

#Quadratura gaussiana para n=3
def quadGaussiana3():
	#valores da tabela para mudanca de variavel para n=3
	t1=-0.7746
	t2=0.0000
	t3=0.7746
	A0=0.5555
	A1=0.8888
	A2=0.5555

	#calculo dos valores de x
	x1=x(t1)
	x2=x(t2)
	x3=x(t3)
	return ((b-a)/2) * (A0*f(i,x1)+A1*f(i,x2)+A2*f(i,x3))

print "valor da Quandratura para n=3 =>",quadGaussiana3()

#Quadratura gaussiana para n=4
def quadGaussiana4():
	#valores da tabela para mudanca de variavel para n=3
	t1=-0.8611
	t2=-0.3400
	t3=0.3400
	t4=0.8611
	A0=0.3478
	A1=0.6521
	A2=0.6521
	A3=0.3478

	#calculo dos valores de x
	x1=x(t1)
	x2=x(t2)
	x3=x(t3)
	x4=x(t4)
	return ((b-a)/2) * (A0*f(i,x1)+A1*f(i,x2)+A2*f(i,x3)+A3*f(i,x4))

print "valor da Quandratura para n=4 =>",quadGaussiana4()

#Quadratura gaussiana para n=5
def quadGaussiana5():
	#valores da tabela para mudanca de variavel para n=5
	t1=-0.9062
	t2=-0.5384
	t3=0.0000
	t4=0.5384
	t5=0.9062
	A0=0.2369
	A1=0.4786
	A2=0.5688
	A3=0.4786
	A4=0.2369

	#calculo dos valores de x
	x1=x(t1)
	x2=x(t2)
	x3=x(t3)
	x4=x(t4)
	x5=x(t5)
	return ((b-a)/2) * (A0*f(i,x1)+A1*f(i,x2)+A2*f(i,x3)+A3*f(i,x4)+A4*f(i,x5))

print "valor da Quandratura para n=5 =>",quadGaussiana5()
