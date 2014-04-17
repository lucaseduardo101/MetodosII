import leitura
import sys
arq = sys.argv[1]

#obtem os dados do arquivo txt
l = leitura.ler(arq)
s = 0
f = []
m=l[0]

x0=l[1][0]
xm=l[m+1][0]

aux=xm-x0
print "xm = ", xm, "x0= ", x0
#Calculo do h
h=aux/m
print "h=", h

for i in range(1,m+2):
	f.append(l[i][1])

aux1=h/2
#Realiza o somatorio
for i in range(1,m):
	print "f[ ",i,"] =", f[i]
	s = s + f[i]
#calculo da formula do trapezio	
aux2=2*s
s1=f[0]+f[m]
s2=aux2+s1

it=aux1*s2 #Calculo final it

print "it =",it
