import leitura
import inteDuplas

import sys
arq = sys.argv[1]

l= leitura.ler(arq) 
f = []

m1 = l[0][0]
m2 = l[0][1]
i = 1
x1	=	l[i][2]    
x2	=	l[i+m1][2]  	
y1	=	l[i][3]
y2	=	l[(m1+1)*(m2+1)][3]

i = 1		
while( i < (m1+1)*(m2+1) ):		
	aux = []
	for j in range (i, i + (m1+1)):
		aux.append(l[j][4])
	f.append(aux)
	i = i + (m1 +1 )
	
print "trapezio"
print inteDuplas.trapezioo( m1, m2, x1, x2, y1, y2, f)
print

print "simpsons"
print inteDuplas.simpson( m1, m2, x1, x2, y1, y2, f )
print 
