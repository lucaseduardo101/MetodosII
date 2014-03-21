import trapezio 
import simpson13

def trapezioo( m1, m2, x1, x2, y1, y2, l ):	
	aux = 0
	s = []
	for i in range( 0, m1 +1 ):		
		aux = aux + trapezio.start( m1, x1, x2, l[i] )		
		s.append(aux)
		aux = 0
	aux = trapezio.start( m2, y1, y2, s )
	aux = aux / (x2 * y2)
	return aux 	
	
def simpson(m1, m2,x1, x2, y1, y2, l):
	aux = 0 
	s = []
	for i in range ( 0, m1 + 1 ):
		aux = simpson13.start( m1, x1, x2, l[i] )	
		s.append(aux)
		aux = simpson13
	aux = simpson13.start(m2, y1, y2, s)
	aux = aux / (x2 * y2)
	return aux 


