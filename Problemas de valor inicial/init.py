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


# implementacao de Lagrange para 3 pontos
def lagrange3(x0, y0, x1, y1, x2, y2,x):
    
    l0 = float((x-x1)*(x-x2))/float((x0-x1)*(x0-x2))
    l1 = float((x-x0)*(x-x2))/float((x1-x0)*(x1-x2))
    l2 = float((x-x0)*(x-x1))/float((x2-x0)*(x2-x1)) 
    
    #teste 
    print "\nL0: %f" % l0
    print "L1: %f" % l1
    print "L2: %f" % l2
    
    e0 = l0 * y0;
    e1 = l1 * y1;
    e2 = l2 * y2;
    
    return e0 + e1 + e2


def Adams_terceira(indice,t0,tempo,h,v0):
	v=[]#vai guardar os valores de v da tabela
	
	print('\n usando RungeKutta terceira ordem')
	#aqui vamos obter os pontos v[i-2],v[i-1] e v[i]
	
	Rk3=RungeKutta_terceira(indice,t0,tempo,h,v0)
	
	#calculando o tempo para a extrapolacao
	t_0=t0
	t_1=t0-h
	t_2=t0-(2*h)
	
	print('\n usando lagrange')
	#agora vamos obter as derivadas desses pontos/usar lagrange
	v_linha0=lagrange3(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],t_0)
	v_linha1=lagrange3(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],t_1)
	v_linha2=lagrange3(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],t_2)
	
	print('\n variaveis do metodo preditor-corretor')
	v.append(v0)
	for i in range(0,n-1):
		vt=v[i]#aqui vou pegar o valor anterior calculado
		t=tempo[i]#aqui vou pagar o valor do tempo

				
		# aqui estou calculando a formula final para v_barra[i+1] normal
		aux3=(h/12)
		aux4=(23*v_linha2)-(16*v_linha1)+(5*v_linha0)
		vbarra=vt+(aux3*aux4)
		print '\nvbarra',vbarra
		
		# aqui estou calculando a formula final para v_barra'[i+1]
		aux5=vbarra
		aux6=tempo[i+1]
		vbarra_linha=f(indice,aux6,aux5)
		print 'vbarra_linha=',vbarra_linha

		# aqui estou calculando a formula final para v[i+1]
		soma=(5*vbarra_linha)+(8*v_linha2)-(v_linha1)
		y_atual=vt+((h/12)*soma)
		v.append(y_atual)
	return v
	
print ('\n-------------Metodo Preditor-Corretor de Adams de terceira ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
#imprimindo o vetor com valores da velocidade	
velocidade=Adams_terceira(i,t0,tempo,h,v0)
print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade


#implementacao interpolacao lagrange para 4 pontos
def lagrange4(x0, y0, x1, y1, x2, y2, x3, y3, x):
    
    l0 = float((x-x1)*(x-x2)*(x-x3))/float((x0-x1)*(x0-x2)*(x0-x3))
    l1 = float((x-x0)*(x-x2)*(x-x3))/float((x1-x0)*(x1-x2)*(x1-x3))
    l2 = float((x-x0)*(x-x1)*(x-x3))/float((x2-x0)*(x2-x1)*(x2-x3)) 
    l3 = float((x-x0)*(x-x1)*(x-x2))/float((x3-x0)*(x3-x1)*(x3-x2))
    
    print "L0: %f" % l0
    print "L1: %f" % l1
    print "L2: %f" % l2
    print "L3: %f" % l3
     
    e0 = l0 * y0;
    e1 = l1 * y1;
    e2 = l2 * y2;
    e3 = l3 * y3;
    
    return e0 + e1 + e2 + e3

#preditor-corretor de Adams de quarta ordem
def Adams_quarta(indice,t0,tempo,h,v0):
	v=[]#vai guardar os valores de v da tabela
	
	print('\n usando RungeKutta terceira ordem')
	#aqui vamos obter os pontos v[i-3],v[i-2],v[i-1] e v[i]
	Rk3=RungeKutta_quarta(indice,t0,tempo,h,v0)
	
	#calculando o tempo para a extrapolacao
	t_0=t0
	t_1=t0-h
	t_2=t0-(2*h)
	t_3=t0-(3*h)
	
	
	print('\n usando lagrange')
	#agora vamos obter as derivadas desses pontos/usar lagrange
	v_linha0=lagrange4(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],tempo[3],Rk3[3],t_0)
	v_linha1=lagrange4(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],tempo[3],Rk3[3],t_1)
	v_linha2=lagrange4(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],tempo[3],Rk3[3],t_2)
	v_linha3=lagrange4(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],tempo[3],Rk3[3],t_3)
	
	print('\n variaveis do metodo preditor-corretor')
	v.append(v0)
	for i in range(0,n-1):
		vt=v[i]#aqui vou pegar o valor anterior calculado
		t=tempo[i]#aqui vou pagar o valor do tempo
		
		# aqui estou calculando a formula final para v_barra[i+1] normal
		aux3=(h/24)
		aux4=(55*v_linha0)-(59*v_linha1)+(37*v_linha2)-(9*v_linha3)
		vbarra=vt+(aux3*aux4)
		print '\nvbarra',vbarra
		
		# aqui estou calculando a formula final para v_barra'[i+1]
		aux5=vbarra
		aux6=tempo[i+1]
		vbarra_linha=f(indice,aux6,aux5)
		print 'vbarra_linha=',vbarra_linha

		# aqui estou calculando a formula final para v[i+1]
		soma=(9*vbarra_linha)+(19*v_linha0)-(5*v_linha1)+(v_linha2)
		y_atual=vt+((h/24)*soma)
		v.append(y_atual)
>>>>>>> d8494bd29a3fccafea7319130a035e78cd99ab34
	return v
	
print ('\n-------------Metodo Preditor-Corretor de Adams de quarta ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, h, n )
#imprimindo o vetor com valores da velocidade	

<<<<<<< HEAD
velocidade = adams_terceira( i, t0, tempo, h, v0 )
print ( 'valores coluna tempo:' ), tempo
print ( 'valores coluna velocidade:' ), velocidade

#preditor-corretor de Adams de quarta ordem

=======
velocidade=Adams_quarta(i,t0,tempo,h,v0)
print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade
>>>>>>> d8494bd29a3fccafea7319130a035e78cd99ab34
