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
		exit()

	#testando derivadas para 02 pontos
	BD2= (f (x + h) - f (x-h))/h

	print ('backward Difference 2 pontos='),BD2

	FD2= (f (x + h) - f (x))/h

	print ('Forward Difference 2 pontos='),FD2

	CD2= (f (x + h) - f (x-h))/(2*h)

	print ('central Difference 2 pontos='),CD2

       #testando derivadas para 03 pontos
	BD3= (f(x) - 2*(f (x - h)) + f(x - (2*h)))/h

	print ('backward Difference 3 pontos='),BD3

	FD3 = (f(x+(2*h))-2*(f (x + h)) + f (x))/h

	print ('Forward Difference 3 pontos='),FD3

	CD3= (f (x + h) - (2*f(x))+ f(x-h))/(h**2)

	print ('central Difference 3 pontos='),CD3
