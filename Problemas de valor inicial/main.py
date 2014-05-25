
from init import f,t,euler,RungeKutta_segunda, RungeKutta_terceira, RungeKutta_quarta, Adams_terceira, Adams_quarta 
import leitura,time
import sys


arq = sys.argv[ 1 ]
l = leitura.ler( arq )

v0 = l[ 0 ]#recebe o valor de v0
i = l[ 1 ]#recebe o numero da funcao escolhida
h = l[ 2 ]#recebe o valor de h
t0 = l[ 3 ][ 0 ] #recebe o limite inferior
tn = l[ 3 ][ 1 ] #recebe o limite superior
n = 5 #quantidade de linhas que a tabela vai ter


# Escolha da funcao
# 			------------------------------------------------
#			|	indices	|			        |	
#			-----------------------------------------------		
#			| 	  0     | y'= (v - t + 2)	       |
#			| 	  1  	| y'=(v*(t**3)) - 1.5 * v      |
#			| 	  2 	| y'=(1+(4*t))*math.sqrt(x)    |
#			| 	  3 	| y'=-2*x + t*t		      |
#			|		|
#			----------------------------------------------

print "           ***  Funcao numero: ", i ," *** "
print "           ***  V(0): ", v0 ," *** "
print "           ***  H: ", h ," *** "
print "           ***  t0: ", t0 ," *** "
print "           ***  tn: ", tn ," *** "

#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )

print ( 'valores coluna tempo:' ), tempo
#imprimindo o vetor com valores da velocidade	

velocidade = euler( f, i, v0, tempo, h,  )
print ( 'valores coluna velocidade:' ), velocidade

print ( '\n-------------Metodo RungeKutta_segunda ordem-------------' )
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )

#imprimindo o vetor com valores da velocidade
velocidade = RungeKutta_segunda( f, i, v0, tempo, h )
print ( 'valores coluna tempo:' ), tempo
print ( 'valores coluna velocidade:' ), velocidade

print ( '\n-------------Metodo RungeKutta_terceira ordem-------------' )
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )

#imprimindo o vetor com valores da velocidade	
velocidade = RungeKutta_terceira( f, i, v0, tempo, h )

print ( 'valores coluna tempo:' ), tempo
print ( 'valores coluna velocidade:' ), velocidade

	
print ('\n-------------Metodo RungeKutta_quarta ordem-------------')

#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )
#imprimindo o vetor com valores da velocidade	
velocidade = RungeKutta_quarta( f, i, v0, tempo, h )
print ( 'valores coluna tempo:' ), tempo
print ( 'valores coluna velocidade:' ), velocidade

print ('\n-------------Metodo Preditor-Corretor de Adams de terceira ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )
#imprimindo o vetor com valores da velocidade	
velocidade = Adams_terceira( f, i, tempo, h, v0 )
print ('valores coluna tempo:'), tempo
print ('valores coluna velocidade:'), velocidade

	
print ('\n-------------Metodo Preditor-Corretor de Adams de quarta ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )
#imprimindo o vetor com valores da velocidade	
velocidade = Adams_quarta( f, i, tempo, h, v0)
print ('valores coluna tempo:'), tempo
print ('valores coluna velocidade:'), velocidade
