import leitura
import sys
arq = sys.argv[1]

l = leitura.ler(arq)
x = []
y = []
m = l[0]
somatorio = 0.0
simpson = 0.0

h = (l[m+1][0] - l[1][0]) / m
print h

for i in range ( 1,m +2):
	x.append( l[i][0] )
	y.append( l[i][1] )
	
print x
print y	

for i in range(0,len(y)):
	if ( ( i == 0 ) or ( i == len(x) - 1 ) ): 
		somatorio = y[i] + somatorio		
	elif ( i%3 == 0 ): 
		somatorio = 2.0*y[i] + somatorio
	else: 
		somatorio = 3.0*y[i] +somatorio

simpson = ( (3*h)/8 ) * somatorio

print simpson
	 

 
