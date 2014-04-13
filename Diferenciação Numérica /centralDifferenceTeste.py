import sys
import leitura
from math import sqrt, exp, sin, cos

#arq = sys.argv[1]
#l = leitura.ler(arq)

#n=l[0]#numero de pontos a ser utilizado
#i=l[1]#recebe o numero da funcao escolhida
#h=l[2]#recebe o valor de h -obs: vai ser uma posicao do vetor simples,ajeitar isso
#x=l[3]#recebe o valor de x onde a funcao deve ser diferenciada -obs:ajeitar isso

n=2#numero de pontos a ser utilizado
i=1#recebe o numero da funcao escolhida
h=0.25#recebe o valor de h -obs: vai ser uma posicao do vetor simples,ajeitar isso
x=0.5#recebe o valor de x onde a funcao deve ser diferenciada -obs:ajeitar isso

# 	Escolha da funcao
# 	---------------------------------------------------
#|	indices	|		funcao		          |	
#	--------------------------------------------------		
#	| 1  	| -0.1x^4 -0.15x^3 -0.5x^2 -0.25x +1.2    |
#	| 2  	| 2x^4 -6x^3 -12x -8	                  |
#	| 3 	| 2x^3 + 3x^2 + 6x + 1	                  |
#	| 4  	| 1 -x -4x^3 +2x^5	                  |
#	---------------------------------------------------

print "valor de n:",n
print "funcao numero:",i
print "valor de h:",h
print "valor de x:",x

	
if (i == 1):
	def f(x):
		return (-0.1 * x**4 - 0.15 * x**3 -0.5 * x**2 -0.25 * x +1.2)
elif (i == 2):
	def f(x):
		return (2 * x**4 -6 * x**3 -12 * x -8)
elif (i == 3):
	def f(x):
		return (2 * x**3 + 3 * x**2 + 6 * x + 1)
elif (i == 4):
	def f(x):
		return (1 - x -4 * x**3 + 2 * x **5)	
else:
	print ('Funcao nao definida na tabela.')
	exit()

#testando derivadas para 02 pontos
BD2= (f (x + h) - f (x-h))/h

print ('backward Difference 2 pontos='),BD2

FD2= (f (x + h) - f (x))/h

print ('Forward Difference 2 pontos='),FD2

CD2= (f (x + h) - f (x-h))/(2*h)

print ('central Difference 2 pontos='),CD2

