# -*- coding: utf-8 -*-

def start( m, x0, xm, f ):
	s = 0 
	aux=xm-x0
		
	#Calculo do h
	h=aux/m
	aux1=h/3
	
	#Realiza o somatorio
	for i in range(1,m):
		if(i%2==0):
			s = s + 2.0*f[i]
		else:
			s = s + 4.0*f[i]	

	#calculo da formula de 1/3 Simpson
	s1=f[0]+f[m]
	s2=s+s1
	simpson13 = aux1*s2 #Calculo final

	return simpson13
