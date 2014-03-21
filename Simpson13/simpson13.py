# -*- coding: utf-8 -*-
import leitura
import sys
arq = sys.argv[1] #Recebe o nome do arquivo que será lido  

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

aux1=h/3
#Realiza o somatorio

for i in range(1,m):
	print "f[ ",i,"] =", f[i]
	if(i%2==0):
		s = s + 2.0*f[i]
	else:
		s = s + 4.0*f[i]	

#calculo da formula de 1/3 Simpson
s1=f[0]+f[m]
s2=s+s1
simpson13=aux1*s2 #Calculo final Isr

print "Isr =",simpson13
