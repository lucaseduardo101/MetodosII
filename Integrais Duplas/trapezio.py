# -*- coding: utf-8 -*-

def start( m, x0, xm, f ):
	#obtem os dados do arquivo txt	
	s = 0.0
	aux= xm-x0		
	#Calculo do h
	h=aux/m	
	
	aux1=h/2
		
	#Realiza o somatorio
	for i in range(1,m):
		s = s + f[i]	
		
	#calculo da formula do trapezio		
	aux2=2*s	
	s1=f[0]+f[m]
	s2=aux2+s1
	#Calculo final it	
	it=aux1*s2 
	return it
