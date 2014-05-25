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


#preditor-corretor de Adams de terceira ordem
def Adams_terceira( f, indice, tempo, h, v0 ):
	
	n = len ( tempo )	
	v_ = range( n ) #guarda os valores de v linha
	v  = range ( n ) #guarda os valores de v
	vbarra = range( n )
	vbarra_ = range( n )		
	t = tempo[ 0 ]	
	i = 2 
	
	#aqui vamos obter os pontos v[i-2],v[i-1] e v[i]	
	v = RungeKutta_quarta( f, indice, v0, tempo, h )
		
	v_[0] = ( f( indice, v[0], t) )
	v_[1] = ( f( indice, v[1], t + h )  )
	v_[2] = ( f( indice, v[2], t + 2*h )  )
	
	t = t + 2 * h
	
	while ( i < n - 1 ) :		

		vbarra[ i + 1 ] = v[ i ] + ( h / 12.0 ) * ( 23.0 * v_[i] - 16.0 * v_[ i - 1 ] + 5.0 * v_[ i - 2 ] )
		vbarra_[ i + 1 ] = f( indice, vbarra [ i + 1 ], t + h )        			  
		v[ i + 1 ] = v[ i ] + ( h / 12.0 ) * ( 5.0 * vbarra_[ i + 1 ] + 8.0 * v_[ i ] - v_[ i - 1 ] )
		v_[ i + 1 ] = f( indice, v[ i + 1 ], t + h )
		t = t + h
		i = i + 1 	

	return v


#preditor-corretor de Adams de quarta ordem
def Adams_quarta( f, indice, tempo, h, v0 ):
	
	n = len ( tempo )	
	v_ = range( n ) #guarda os valores de v linha
	v  = range ( n ) #guarda os valores de v
	vbarra = range( n )
	vbarra_ = range( n )		
	t = tempo[ 0 ]	
	i = 3 
	
	#aqui vamos obter os pontos v[i-2],v[i-1] e v[i]	
	v = RungeKutta_quarta( f, indice, v0, tempo, h )
		
	v_[ 0 ] = ( f( indice, v[ 0 ], t ) )
	v_[ 1 ] = ( f( indice, v[ 1 ], t + h )  )
	v_[ 2 ] = ( f( indice, v[ 2 ], t + 2 * h )  )
	v_[ 3 ] = ( f( indice, v[ 3 ], t + 3 * h )  )
	
	t = t + 3 * h
		
	while ( i < n - 1 ) :		

		vbarra[ i + 1 ] = v[ i ] + ( h / 24.0 ) * ( 55.0 * v_[i] - 59.0 * v_[ i - 1 ] + 37.0 * v_[ i - 2 ] - 9.0 * v_[ i - 3 ] )
		
		vbarra_[ i + 1 ] = f( indice, vbarra [ i + 1 ], t + h )        			  
		
		v[ i + 1 ] = v[ i ] + ( h / 24.0 ) * ( 9.0 * vbarra_[ i + 1 ] + 19.0 * v_[ i ] - 5.0 * v_[ i - 1 ] + v_[ i - 2 ]  )
		
		v_[ i + 1 ] = f( indice, v[ i + 1 ], t + h )
		
		t = t + h
		
		i = i + 1 	
		
	return v

