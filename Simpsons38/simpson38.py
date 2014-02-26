import leitura

l = leitura.ler()
m = l[0]

h = (l[m+1][0] - l[1][0]) / m
print h

x = [0.0, 0.5, 1.0,   1.5]
y = [0.0, 0.35, 0.55, 0.9]

somatorio = 0.0
simpson = 0.0	

for i in range(0,len(y)):
	if ( ( i == 0 ) or ( i == len(x) - 1 ) ): 
		somatorio = y[i] + somatorio		
	elif ( i%3 == 0 ): 
		somatorio = 2.0*y[i] + somatorio
	else: 
		somatorio = 3.0*y[i] +somatorio

simpson = ( (3*h)/8 ) * somatorio

print simpson
	 

 
