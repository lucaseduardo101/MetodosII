import derivada1

def extraRichard(h1, i, x):
	h2 = h1/2
	print "Escolha qual metodo utilizar" 
	print "1 ForwardDifference"
	print "2 backwardDifference"
	print "3 centralDifference"
	
	j = int(input())
	if (j == 1 ):
		return (4/3) * derivada1.forwardDifference( 3, i, h2, x) - ( 1/3 ) * derivada1.forwardDifference(3, i, h1, x)  
	elif (j == 2 ):
		return (4/3) * derivada1.backwardDifference( 3, i, h2, x) - ( 1/3 ) * derivada1.backwardDifference(3, i, h1, x)
	elif ( j == 3 ):
		return (4/3) * derivada1.centralDifference( 3, i, h2, x) - ( 1/3 ) * derivada1.centralDifference(3, i, h1, x)
	else: 
		print "Opcao invalida"

