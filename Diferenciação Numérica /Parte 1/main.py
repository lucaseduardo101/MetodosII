import sys
import leitura
import derivada1
import derivada2

arq = sys.argv[1]
l = leitura.ler(arq)

n=l[0]#numero de pontos a ser utilizado
i=l[1]#recebe o numero da funcao escolhida
h=l[2]#recebe o valor de h -obs: vai ser uma posicao do vetor simples,ajeitar isso
x=l[3]#recebe o valor de x onde a funcao deve ser diferenciada -obs:ajeitar isso

#n=4#numero de pontos a ser utilizado
#i=1#recebe o numero da funcao escolhida
#h=0.5#recebe o valor de h -obs: vai ser uma posicao do vetor simples,ajeitar isso
#x=0.5#recebe o valor de x onde a funcao deve ser diferenciada -obs:ajeitar isso



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

print "Derivada 1 "
#centralDifference(n,i,h,x)
derivada1.centralDifference(n,i,h,x)
derivada1.forwardDifference(n, i, h, x)
derivada1.backwardDifference(n,i,h,x)


