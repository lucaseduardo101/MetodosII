from math import sqrt, exp, sin, cos


def centralDifference(n, i, h, x): 	
	
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
		return 0
		
	#testando derivadas para 02 pontos
	if ( n ==2 ):
		CD2= (f (x + h) - f (x-h))/(2*h)
		print ('central Difference 2 pontos='),CD2
		return CD2
	elif (n == 3):
		CD3= (f (x + h) - (2*f(x))+ f(x-h))/(h**2)
		print ('central Difference 3 pontos='),CD3
		return CD3
		
	#central Difference para 04 pontos
	elif (n == 4):
		CD4= ((-1*f(x+(2*h)))+ 8*(f (x + h))-8*(f (x-h))+ f(x - (2*h)))/(12*h)
		print ('central Difference 4 pontos='),CD4
		return CD4
	else:
		print "Qtd de pontos nao valida" 
		return 0
	
def backwardDifference(n, i, h, x): 	
	
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
		return 0

	#testando derivadas para 02 pontos
	
	if(n == 2):
		BD2= ( f (x) - f (x-h)) /h
		print ('backward Difference 2 pontos='),BD2
		return BD2
		
	elif(n == 3):
       #testando derivadas para 03 pontos
		BD3= ((3.0*f(x)) - (4.0 * f (x - h)) + f(x - (2.0*h))) / (2.0*h)
		print ('backward Difference 3 pontos='),BD3
		return BD3
	else:
		print "Qtd de pontos nao valida" 
		return 0
		
def forwardDifference(n, i, h, x):
	
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
		return 0

	#testando derivadas para 02 pontos
	if (n == 2):
		FD2= (f (x + h) - f (x))/h
		print ('Forward Difference 2 pontos='),FD2
		return FD2
	elif (n == 3 ):
		FD3 =  (-1.0 * f(x+(2*h)) + 4.0*f (x + h) - 3.0 *f (x)) / (2.0*h)		
		print ('Forward Difference 3 pontos='),FD3
		return FD3
	else:
		print "Qtd de pontos nao valida" 
		return 0
