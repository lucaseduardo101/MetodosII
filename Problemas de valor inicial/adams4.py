#metodo de Runge-kutta de terceira ordem 
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


#implementacao interpolacao lagrange para 4 pontos
def lagrange4(x0, y0, x1, y1, x2, y2, x3, y3, x):
    
    l0 = float((x-x1)*(x-x2)*(x-x3))/float((x0-x1)*(x0-x2)*(x0-x3))
    l1 = float((x-x0)*(x-x2)*(x-x3))/float((x1-x0)*(x1-x2)*(x1-x3))
    l2 = float((x-x0)*(x-x1)*(x-x3))/float((x2-x0)*(x2-x1)*(x2-x3)) 
    l3 = float((x-x0)*(x-x1)*(x-x2))/float((x3-x0)*(x3-x1)*(x3-x2))
    
    print "L0: %f" % l0
    print "L1: %f" % l1
    print "L2: %f" % l2
    print "L3: %f" % l3
     
    e0 = l0 * y0;
    e1 = l1 * y1;
    e2 = l2 * y2;
    e3 = l3 * y3;
    
    return e0 + e1 + e2 + e3

#preditor-corretor de Adams de quarta ordem
def Adams_quarta(indice,t0,tempo,h,v0):
	v=[]#vai guardar os valores de v da tabela
	
	print('\n usando RungeKutta terceira ordem')
	#aqui vamos obter os pontos v[i-3],v[i-2],v[i-1] e v[i]
	Rk3=RungeKutta_terceira(indice,t0,tempo,h,v0)
	
	#calculando o tempo para a extrapolacao
	t_0=t0
	t_1=t0-h
	t_2=t0-(2*h)
	t_3=t0-(3*h)
	
	
	print('\n usando lagrange')
	#agora vamos obter as derivadas desses pontos/usar lagrange
	v_linha0=lagrange4(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],tempo[3],Rk3[3],t_0)
	v_linha1=lagrange4(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],tempo[3],Rk3[3],t_1)
	v_linha2=lagrange4(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],tempo[3],Rk3[3],t_2)
	v_linha3=lagrange4(t0, v0, tempo[1], Rk3[1],tempo[2],Rk3[2],tempo[3],Rk3[3],t_3)
	
	print('\n variaveis do metodo preditor-corretor')
	v.append(v0)
	for i in range(0,n-1):
		vt=v[i]#aqui vou pegar o valor anterior calculado
		t=tempo[i]#aqui vou pagar o valor do tempo
		
		# aqui estou calculando a formula final para v_barra[i+1] normal
		aux3=(h/24)
		aux4=(55*v_linha0)-(59*v_linha1)+(37*v_linha2)-(9*v_linha3)
		vbarra=vt+(aux3*aux4)
		print '\nvbarra',vbarra
		
		# aqui estou calculando a formula final para v_barra'[i+1]
		aux5=vbarra
		aux6=tempo[i+1]
		vbarra_linha=f(indice,aux6,aux5)
		print 'vbarra_linha=',vbarra_linha

		# aqui estou calculando a formula final para v[i+1]
		soma=(9*vbarra_linha)+(19*v_linha0)-(5*v_linha1)+(v_linha2)
		y_atual=vt+((h/24)*soma)
		v.append(y_atual)
	return v
	
print ('\n-------------Metodo Preditor-Corretor de Adams de quarta ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo=t(t0,tn,h,n)
#imprimindo o vetor com valores da velocidade	
velocidade=Adams_quarta(i,t0,tempo,h,v0)
print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade
