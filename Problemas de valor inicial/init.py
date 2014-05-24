from math import sqrt, exp, sin, cos,radians


#selecionaFunc(funcao)
def f( indice, v, t ):
		
	if 	indice == 0:
		return ( v - t + 2 )
	
	elif  indice == 1:
		return ( v * ( t ** 3 ) ) - 1.5  *  v
	
	elif indice == 2:
	    return ( 1 + ( 4 * t ) ) * sqrt( v )
	
	elif indice == 3:
		return - 2 * v + t * t
	
	else:
		print ( 'Funcao nao definida na tabela.' )
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
def euler( f, indice, x0, t, h ):
	n = len(t)
	x = range(n)
	x[0] = x0
	
	for i in range( 0, n-1 ):
		k1 = h * f ( indice, x[i], t[i] )
		x[ i+1 ] = x[i] + k1
		
	return x

	
print ('\n-------------Metodo Forward Euler-------------')

#metodo de Runge-kutta de segunda ordem -baseado na regra do trapezio

def RungeKutta_segunda( f, indice, x0, t, h ):
	n = len(t)
	x = range(n)
	x[0] = x0
	
	for i in xrange(n - 1):
		
		k1 = h * f(  indice, x[i], t[i] )
		
		k2 = h * f(  indice,  x[i] + k1, t[i+1] )
		
		x[i+1] = x[i] + ( k1 + k2 ) / 2.0
		
	return x

#metodo de Runge-kutta de terceira ordem-baseado na regra 1/3 de simpson

def RungeKutta_terceira( f, indice, x0, t, h ):
	n = len( t )
	x = range( n )
	x[0] = x0
	
	for i in xrange(n - 1):
		
		k1 = h * f( indice, x[i], t[i] )
		
		k2 = h * f( indice, x[i] + k1/2.0, t[i] + h/2.0 )
		
		k3 = h * f( indice, x[i] - k1 + 2.0*k2, t[i] + h )
		
		x[i+1] = x[i] + ( k1 + 4.0*k2 +k3 ) / 6.0
	return x

#metodo de Runge-kutta de quarta ordem- baseado na regra 3/8 de simpson

def RungeKutta_quarta( f, indice, x0, t, h ):
	n = len( t )
	x = range(n)
	x[0] = x0
	for i in xrange( n - 1 ):
		k1 = h * f( indice, x[i], t[i] )
		
		k2 = h * f( indice, x[i] + k1 / 3.0, t[i] + h / 3.0 )
		
		k3 = h * f( indice , x[i] + k1 / 3.0 + k2 / 3.0, t[i] + ( 2.0 * h ) / 3.0 )
		
		k4 = h * f( indice, x[i] + k1 - k2 + k3, t[i] + h )
		
		x[i+1] = x[i] + ( k1 + 3.0 * k2 + 3.0 * k3 + k4 ) / 8.0
	return x


# implementacao de Lagrange para 3 pontos

def lagrange3( x0, y0, x1, y1, x2, y2, x ):
    
    l0 = float( ( x - x1 ) * ( x - x2 ) ) / float ( ( x0 - x1 ) * ( x0 - x2 ) )
    l1 = float( ( x - x0 ) * ( x - x2 ) ) /float ( ( x1 - x0 ) * ( x1 - x2 ) )
    l2 = float( ( x - x0 ) * ( x - x1 ) ) /float( ( x2 - x0 ) * ( x2 - x1 ) ) 
    
    #teste 
    print "\nL0: %f" % l0
    print "L1: %f" % l1
    print "L2: %f" % l2
    
    e0 = l0 * y0;
    e1 = l1 * y1;
    e2 = l2 * y2;
    
    return e0 + e1 + e2


#preditor-corretor de Adams de terceira ordem
def Adams_terceira( f, indice, tempo, h, v0 ):
	n = len ( tempo )	
	v_ = range(n) #vai guardar os valores de v da tabela
	v = range(n)
	t = range(n)	
	print( '\n usando RungeKutta terceira ordem' )
	
	#aqui vamos obter os pontos v[i-2],v[i-1] e v[i]	
	Rk3 = RungeKutta_terceira( f, indice, v0, tempo, h )
	
	v.append ( Rk3[0] )
	v.append ( Rk3[1] )
	v.append ( Rk3[2] )
	
	v_.append ( Rk3[0] )
	v_.append ( Rk3[1] )
	v_.append ( Rk3[2] )
	
	t.append( tempo[0] )
	t.append( tempo[1] )  
	t.append( tempo[2] )
			
	for i in range( 3, n - 1 ):		
		
		print('\n usando lagrange')
		#agora vamos obter as derivadas desses pontos/usar lagrange
		v_[i] = lagrange3( t[ i - 3 ], v_[ i - 3 ], t[ i - 2 ], v_[ i - 2 ], t[ i - 1 ], v_[ i - 1 ], t[ i ] )
		
		# aqui estou calculando a formula final para v_barra[i+1] normal
		aux3=( h / 12 )
		aux4=( 23 * v_[ i ])-( 16 * v_[ i - 1 ] ) + ( 5 * v_[ i - 2] )
		vbarra = v[i] + (aux3*aux4)
		print '\nvbarra',vbarra
		
		# aqui estou calculando a formula final para v_barra'[i+1]
		aux5 = vbarra
		aux6 = tempo[ i + 1]
		vbarra_linha = f( indice, aux6, aux5 )
		print 'vbarra_linha=', vbarra_linha

		# aqui estou calculando a formula final para v[i+1]
		soma=( 5* vbarra_linha ) + ( 8 * v_[ i ] ) - ( v_[ i - 1] )
		v_atual = v[ i ] + ( ( h/12 ) * soma )
		v.append(v_atual)	
	
		t.append( tempo[i] )
		t.append( tempo[i] - h )  
		t.append( tempo[i] - (2*h) )
			
		
	return v

#implementacao interpolacao lagrange para 4 pontos
def lagrange4( x0, y0, x1, y1, x2, y2, x3, y3, x ):
    
    l0 = float( ( x - x1 ) * ( x - x2 ) * ( x - x3 ) ) / float( ( x0 - x1 ) * ( x0 - x2 ) * ( x0 - x3 ) )
    l1 = float( ( x - x0 ) * ( x - x2 ) * ( x - x3 ) ) / float( ( x1 - x0 ) * ( x1 - x2 ) * ( x1 - x3 ) )
    l2 = float( ( x - x0 ) * ( x - x1 ) * ( x - x3 ) ) / float( ( x2 - x0 ) * ( x2 - x1 ) * ( x2 - x3 ) ) 
    l3 = float ( ( x -x0 ) * ( x - x1 ) * ( x - x2 ) ) / float( ( x3 - x0) * ( x3 - x1 )  * ( x3 - x2 ) )
    
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
def Adams_quarta( f, indice, t0, tempo, h, v0 ):
	v = [] #vai guardar os valores de v da tabela
	
	print ( '\n usando RungeKutta terceira ordem' )
	#aqui vamos obter os pontos v[i-3],v[i-2],v[i-1] e v[i]
	
	#Rk3 = RungeKutta_quarta ( indice, t0, tempo, h, v0 )
	Rk4 = RungeKutta_quarta( f, indice, v0, tempo, h )
	
	#calculando o tempo para a extrapolacao
	t_0 = t0
	t_1 = t0 - h
	t_2 = t0 - ( 2 * h )
	t_3 = t0 -( 3 * h )
	
	
	print('\n usando lagrange')
	#agora vamos obter as derivadas desses pontos/usar lagrange
	v_linha0=lagrange4(t0, v0, tempo[1], Rk4[1],tempo[2],Rk4[2],tempo[3],Rk4[3],t_0)
	v_linha1=lagrange4(t0, v0, tempo[1], Rk4[1],tempo[2],Rk4[2],tempo[3],Rk4[3],t_1)
	v_linha2=lagrange4(t0, v0, tempo[1], Rk4[1],tempo[2],Rk4[2],tempo[3],Rk4[3],t_2)
	v_linha3=lagrange4(t0, v0, tempo[1], Rk4[1],tempo[2],Rk4[2],tempo[3],Rk4[3],t_3)
	
	print('\n variaveis do metodo preditor-corretor')
	v.append( v0 )
	for i in range( 0, n-1 ):
		vt = v[ i ]#aqui vou pegar o valor anterior calculado
		t = tempo[ i ]#aqui vou pagar o valor do tempo
		
		# aqui estou calculando a formula final para v_barra[i+1] normal
		aux3 = ( h/24 )
		aux4 = ( 55*v_linha0)-(59*v_linha1)+(37*v_linha2)-(9*v_linha3)
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
	return v

