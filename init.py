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
def f(indice,x,y):	
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
	f0=f(i,t0,v0)
	
	v=[]#vai guardar os valores de v da tabela
	y1=v0+(h*f0)
	v.append(y1)
	
	for i in range(0,n-1):
		vt=v[i-1]#aqui vou pegar o valor anterior calculado
		t=tempo[i]#aqui vou pagar o valor do tempo
		fn=f(0,t,vt)#aqui vou calcular a funcao com os valores das duas variaveis
		y_atual=vt+(h*fn)
		v.append(y_atual)
	return v

print ('\n-------------Metodo Forward Euler-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
print ('valores coluna tempo:'),tempo
#imprimindo o vetor com valores da velocidade	
velocidade=euler(i,t0,tempo,h,v0)
print ('valores coluna velocidade:'),velocidade


#metodo de Runge-kutta de segunda ordem (conhecido como metodo de Euler Modificado)
def RungeKutta_segunda(indice,t0,tempo,h,v0):
	f0=f(indice,t0,v0)
	v=[]#vai guardar os valores de v da tabela
	y1=v0+(h*f0)
	v.append(y1)
	
		
	for i in range(0,n-1):
		vt=v[i]#aqui vou pegar o valor anterior calculado
		t=tempo[i]#aqui vou pagar o valor do tempo

		k1=f(indice,t,vt)
		print 'k1=',k1
	
		aux1=t+(h/2)
		aux2=vt+((h/2)*k1)
		k2=f(indice,aux1,aux2)
		print 'k2=',k2

		y_atual=vt+(h*k2)
		v.append(y_atual)
	return v
	
print ('\n-------------Metodo RungeKutta_segunda ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
#imprimindo o vetor com valores da velocidade	
velocidade=RungeKutta_segunda(i,t0,tempo,h,v0)
print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade


#metodo de Runge-kutta de terceira ordem (conhecido como metodo de Euler Modificado)
def RungeKutta_terceira(indice,t0,tempo,h,v0):
	f0=f(indice,t0,v0)
	v=[]#vai guardar os valores de v da tabela
	y1=v0+(h*f0)
	v.append(y1)
	
		
	for i in range(0,n-1):
		vt=v[i]#aqui vou pegar o valor anterior calculado
		t=tempo[i]#aqui vou pagar o valor do tempo

		k1=f(indice,t,vt)
		print 'k1=',k1
	
		aux1=t+(h/3)
		aux2=vt+((h/3)*k1)
		k2=f(indice,aux1,aux2)
		print 'k2=',k2
		
		aux3=t+(2*(h/3))
		aux4=vt+((2*(h/3))*k2)
		k3=f(indice,aux3,aux4)
		print 'k3=',k3

		soma=k1+(3*k3)
		y_atual=vt+((h/4)*soma)
		v.append(y_atual)
	return v
	
print ('\n-------------Metodo RungeKutta_terceira ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
#imprimindo o vetor com valores da velocidade	
velocidade=RungeKutta_terceira(i,t0,tempo,h,v0)
print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade



#metodo de Runge-kutta de quarta ordem (conhecido como metodo de Euler Modificado)
def RungeKutta_quarta(indice,t0,tempo,h,v0):
	f0=f(indice,t0,v0)
	v=[]#vai guardar os valores de v da tabela
	y1=v0+(h*f0)
	v.append(y1)
	
		
	for i in range(0,n-1):
		vt=v[i]#aqui vou pegar o valor anterior calculado
		t=tempo[i]#aqui vou pagar o valor do tempo

		k1=f(indice,t,vt)
		print 'k1=',k1
	
		aux1=t+(h/2)
		aux2=vt+((h/2)*k1)
		k2=f(indice,aux1,aux2)
		print 'k2=',k2
		
		aux3=t+(h/2)
		aux4=vt+((h/2)*k2)
		k3=f(indice,aux3,aux4)
		print 'k3=',k3
		
		aux5=t+h
		aux6=vt+(h*k3)
		k4=f(indice,aux5,aux6)
		print 'k4=',k4

		soma=k1+(2*(k2+k3))+k4
		y_atual=vt+((h/6)*soma)
		v.append(y_atual)
	return v
	
print ('\n-------------Metodo RungeKutta_quarta ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
#imprimindo o vetor com valores da velocidade	
velocidade=RungeKutta_quarta(i,t0,tempo,h,v0)
print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade
