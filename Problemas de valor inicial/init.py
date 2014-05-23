import sys
import leitura,time
from math import sqrt, exp, sin, cos,radians

arq = sys.argv[1]
l = leitura.ler( arq )

v0 = l[0]#recebe o valor de v0
i = l[1]#recebe o numero da funcao escolhida
h = l[2]#recebe o valor de h
t0 = l[3][0] #recebe o limite inferior
tn = l[3][1] #recebe o limite superior
n = 4 #quantidade de linhas que a tabela vai ter


# Escolha da funcao
# 			-----------------------------------------
#			|	indices	|			|	
#			-----------------------------------------		
#			| 	  0     | y'= -y + x + 2	|
#			| 	  1  	|	    	|
#			| 	  2 	|   		|
#			| 	  3 	|		|
#			|		|
#			-----------------------------------------

print "           ***  Funcao numero: ", i ," *** "
print "           ***  V(0): ", v0 ," *** "
print "           ***  H: ", h ," *** "
print "           ***  t0: ", t0 ," *** "
print "           ***  tn: ", tn ," *** "

#selecionaFunc(funcao)
def f( indice, v, t ):	
	if 	indice == 0:
		return ( v - t + 2 )
	elif  indice == 1:
		return ( v * ( t ** 3 ) ) - 1.5  *  v
	elif indice == 2:
	    return ( 1 + ( 4 * t ) ) * math.sqrt( x )
	elif indice == 3:
		return -2 * x + t * t
	else:
		print ('Funcao nao definida na tabela.')
		exit()

#funcao que calcula os valores de t que serao usados no intervalo

def t( t0, tn, h, n ):
	t = []#vai guardar os valores da coluna t da tabela
	t.append( t0 )
	aux = t0
	for i in range( 1, n-1 ):
		aux = aux + h
		t.append( aux )

	t.append( tn )	
	return t


#Metodo Forward Euler
def euler( i, t0, tempo, h, v0 ):
	f0 = f( i, v0, t0 )
	
	v = []#vai guardar os valores de v da tabela
	v1 = v0 + ( h * f0 )
	v.append( v1 )
	
	for i in range( 0, n-1 ):
		vi = v[i-1]#aqui vou pegar o valor anterior calculado
		ti = tempo[i]#aqui vou pagar o valor do tempo
		fn = f( 0, vi, ti )#aqui vou calcular a funcao com os valores das duas variaveis
		v_atual = vi + ( h * fn )
		v.append( v_atual )
	return v

	
print ('\n-------------Metodo Forward Euler-------------')

#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, h, n )

print ('valores coluna tempo:'), tempo
#imprimindo o vetor com valores da velocidade	

velocidade = euler( i, t0, tempo, h, v0 )
print ('valores coluna velocidade:'), velocidade


#metodo de Runge-kutta de segunda ordem -baseado na regra do trapezio
def RungeKutta_segunda( f, indice, x0, t, h ):
	n = len(t)
	x = range(n)
	x[0] = x0
	
	for i in xrange(n - 1):
		k1 = h * f(  indice, x[i], t[i] )
		print "k1= ",k1
		k2 = h * f(  indice,  x[i] + k1, t[i+1] )
		print "k2= ",k2
		x[i+1] = x[i] + ( k1 + k2 ) / 2.0
	return x


	
print ('\n-------------Metodo RungeKutta_segunda ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, h, n )

#imprimindo o vetor com valores da velocidade
velocidade = RungeKutta_segunda( f, i, v0, tempo, h )
print ( 'valores coluna tempo:' ), tempo
print ( 'valores coluna velocidade:' ), velocidade

#metodo de Runge-kutta de terceira ordem-baseado na regra 1/3 de simpson

def RungeKutta_terceira( f, indice, x0, t, h ):
	n = len( t )
	x = range( n )
	x[0] = x0
	for i in xrange(n - 1):
		k1 = h * f( indice, x[i], t[i] )
		print "K1=", k1
		k2 = h * f( indice, x[i] + k1/2.0, t[i] + h/2.0 )
		print "K2=", k2
		k3 = h * f( indice, x[i] - k1 + 2.0*k2, t[i] + h )
		print "K3=", k3
		x[i+1] = x[i] + ( k1 + 4.0*k2 +k3 ) / 6.0
	return x

	
print ( '\n-------------Metodo RungeKutta_terceira ordem-------------' )
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, h, n )

#imprimindo o vetor com valores da velocidade	
velocidade = RungeKutta_terceira( f, i, v0, tempo, h )

print ( 'valores coluna tempo:' ), tempo
print ( 'valores coluna velocidade:' ), velocidade


#metodo de Runge-kutta de quarta ordem- baseado na regra 3/8 de simpson

def RungeKutta_quarta(f, indice, x0, t, h):
	n = len( t )
	x = range(n)
	x[0] = x0
	for i in xrange( n - 1 ):
		k1 = h * f( indice, x[i], t[i] )
		print "K1=", k1
		k2 = h * f( indice, x[i] + k1 / 3.0, t[i] + h / 3.0 )
		print "K2=", k2
		k3 = h * f( indice , x[i] + k1 / 3.0 + k2 / 3.0, t[i] + ( 2.0 * h ) / 3.0 )
		print "K3=", k3
		k4 = h * f( indice, x[i] + k1 - k2 + k3, t[i] + h )
		print "K4=", k4
		x[i+1] = x[i] + ( k1 + 3.0 * k2 + 3.0 * k3 + k4 ) / 8.0
	return x

	
print ('\n-------------Metodo RungeKutta_quarta ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, h, n )
#imprimindo o vetor com valores da velocidade	
velocidade = RungeKutta_quarta( f, i, v0, tempo, h )
print ( 'valores coluna tempo:' ), tempo
print ( 'valores coluna velocidade:' ), velocidade



#implementacao interpolacao lagrange para 3 pontos
def lagrange( x0, y0, x1, y1, x2, y2, x ):
    
    l0 = float( ( x - x1 ) * ( x - x2 ) ) / float ( ( x0 - x1 ) * ( x0 - x2 ) )
    l1 = float( ( x - x0 ) * ( x - x2 ) ) / float ( ( x1 - x0 ) * ( x1 - x2 ) )
    l2 = float( ( x - x0 ) * ( x - x1 ) ) / float ( ( x2 - x0 ) * ( x2 - x1 ) ) 
    
    #teste 
    print "\nL0: %f" % l0
    print "L1: %f" % l1
    print "L2: %f" % l2
    
    e0 = l0 * y0;
    e1 = l1 * y1;
    e2 = l2 * y2;
    
    return e0 + e1 + e2

result = lagrange( 0, 0, 1, 2, 5, 8, 7 )


print "Lagrange v'(x)= %d" % result


#preditor-corretor de Adams de terceira ordem
def adams_terceira( indice, t0, tempo, h, v0 ):
	f0 = f( indice, v0, t0 )
	v = []#vai guardar os valores de v da tabela
	v1 = v0 +( h * f0 )
	v.append( v1 )
	
		
	for i in range( 0, n-1 ):
		vi = v[i]#aqui vou pegar o valor anterior calculado
		ti = tempo[i]#aqui vou pagar o valor do tempo

		k1 = h * ( f( indice, vi, ti ) )
		print 'k1=', k1
	
		aux1 = vi + ( k1 / 3 )
		aux2 = ti + ( h / 3 )
		k2 = h * ( f( indice, aux1, aux2 ) )
		print 'k2=', k2
		
		aux3 = vi + ( k1 / 3 ) + ( k2 / 3 )
		aux4 = ti + ( ( 2 * h ) / 3 )
		k3 = h * ( f ( indice, aux3, aux4 ) )
		print 'k3=', k3
		
		aux5 = vi + k1 - k2 + k3
		aux6 = ti + h
		k4 = h * ( f ( indice, aux3, aux4 ) )
		print 'k4=', k4
		
		aux7 = k1 + ( 3 * k2 ) + ( 3 * k3 ) + k4
		v_atual = vi + ( aux7 / 8 ) 
		v.append( v_atual )
	return v
	
print ('\n-------------preditor-corretor de Adams de terceira ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, h, n )
#imprimindo o vetor com valores da velocidade	
velocidade = adams_terceira( i, t0, tempo, h, v0 )
print ( 'valores coluna tempo:' ), tempo
print ( 'valores coluna velocidade:' ), velocidade

#preditor-corretor de Adams de quarta ordem

