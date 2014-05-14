import sys
import leitura,time
from math import sqrt, exp, sin, cos,radians

arq = sys.argv[1]
l = leitura.ler(arq)

v0=l[0]#recebe o valor de v0
i=l[1]#recebe o numero da funcao escolhida
h=l[2]#recebe o valor de h
t0=l[3][0] #recebe o limite inferior
tn=l[3][1] #recebe o limite superior
n=4 #quantidade de linhas que a tabela vai ter


# Escolha da funcao
# 			-----------------------------------------
#			|	indices	|			|	
#			-----------------------------------------		
#			| 	  0     | y'= -y + x + 2	|
#			| 	  1  	|	    	|
#			| 	  2 	|   		|
#			| 	  3 	|		|
#			|		|
#			-----------------------------------------

print "           ***  Funcao numero: ",i," *** "

#selecionaFunc(funcao)
def f(indice,y,x):	
	if (indice == 0):
		return (x - y + 2)
	
	else:
		print ('Funcao nao definida na tabela.')
		exit()

#funcao que calcula os valores de t que serao usados no intervalo
def t(t0,tn,h,n):
	t=[]#vai guardar os valores da coluna t da tabela
	t.append(t0)
	aux=t0
	for i in range(1,n-1):
		aux=aux+h
		t.append(aux)

	t.append(tn)
	
	return t


#Metodo Forward Euler
def euler(i,t0,tempo,h,v0):
	f0=f(i,v0,t0)
	
	v=[]#vai guardar os valores de v da tabela
	v1=v0+(h*f0)
	v.append(v1)
	
	for i in range(0,n-1):
		vi=v[i-1]#aqui vou pegar o valor anterior calculado
		ti=tempo[i]#aqui vou pagar o valor do tempo
		fn=f(0,vi,ti)#aqui vou calcular a funcao com os valores das duas variaveis
		v_atual=vi+(h*fn)
		v.append(v_atual)
	return v

print ('\n-------------Metodo Forward Euler-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
print ('valores coluna tempo:'),tempo
#imprimindo o vetor com valores da velocidade	
velocidade=euler(i,t0,tempo,h,v0)
print ('valores coluna velocidade:'),velocidade


#metodo de Runge-kutta de segunda ordem -baseado na regra do trapezio
def RungeKutta_segunda(indice,t0,tempo,h,v0):
	f0=f(indice,v0,t0)
	v=[]#vai guardar os valores de v da tabela
	v1=v0+(h*f0)
	v.append(v1)
	
		
	for i in range(0,n-1):
		vi=v[i]#aqui vou pegar o valor anterior calculado
		ti=tempo[i]#aqui vou pagar o valor do tempo

		k1=h*(f(indice,vi,ti))
		print 'k1=',k1
	
		aux1=vi+k1
		aux2=tempo[i+1]
		k2=h*(f(indice,aux1,aux2))
		print 'k2=',k2

		v_atual=vi+((k1+k2)/2)
		v.append(v_atual)
	return v
	
print ('\n-------------Metodo RungeKutta_segunda ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
#imprimindo o vetor com valores da velocidade	
velocidade=RungeKutta_segunda(i,t0,tempo,h,v0)
print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade


#metodo de Runge-kutta de terceira ordem-baseado na regra 1/3 de simpson
def RungeKutta_terceira(indice,t0,tempo,h,v0):
	f0=f(indice,v0,t0)
	v=[]#vai guardar os valores de v da tabela
	v1=v0+(h*f0)
	v.append(v1)
	
		
	for i in range(0,n-1):
		vi=v[i]#aqui vou pegar o valor anterior calculado
		ti=tempo[i]#aqui vou pagar o valor do tempo

		k1=h*(f(indice,vi,ti))
		print 'k1=',k1
	
		aux1=vi+(k1/2)
		aux2=ti+(h/2)
		k2=h*(f(indice,aux1,aux2))
		print 'k2=',k2
		
		aux3=vi-k1+(2*k2)
		aux4=ti+h
		k3=h*(f(indice,aux3,aux4))
		print 'k3=',k3
		
		aux5=k1+(4*k2)+k3
		v_atual=vi+(aux5/6)
		v.append(v_atual)
	return v
	
print ('\n-------------Metodo RungeKutta_terceira ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
#imprimindo o vetor com valores da velocidade	
velocidade=RungeKutta_terceira(i,t0,tempo,h,v0)
print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade



#metodo de Runge-kutta de quarta ordem- baseado na regra 3/8 de simpson
def RungeKutta_quarta(indice,t0,tempo,h,v0):
	f0=f(indice,v0,t0)
	v=[]#vai guardar os valores de v da tabela
	v1=v0+(h*f0)
	v.append(v1)
	
		
	for i in range(0,n-1):
		vi=v[i]#aqui vou pegar o valor anterior calculado
		ti=tempo[i]#aqui vou pagar o valor do tempo

		k1=h*(f(indice,vi,ti))
		print 'k1=',k1
	
		aux1=vi+(k1/3)
		aux2=ti+(h/3)
		k2=h*(f(indice,aux1,aux2))
		print 'k2=',k2
		
		aux3=vi+(k1/3)+(k2/3)
		aux4=ti+((2*h)/3)
		k3=h*(f(indice,aux3,aux4))
		print 'k3=',k3
		
		aux5=vi+k1-k2+k3
		aux6=ti+h
		k4=h*(f(indice,aux3,aux4))
		print 'k4=',k4
		
		aux7=k1+(3*k2)+(3*k3)+k4
		v_atual=vi+(aux7/8)
		v.append(v_atual)
	return v
	
print ('\n-------------Metodo RungeKutta_quarta ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
#imprimindo o vetor com valores da velocidade	
velocidade=RungeKutta_quarta(i,t0,tempo,h,v0)
print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade

#preditor-corretor de Adams de terceira ordem
#preditor-corretor de Adams de quarta ordem
