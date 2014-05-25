#Programa gerar graficos 

from init import f,t,euler,RungeKutta_segunda, RungeKutta_terceira, RungeKutta_quarta, Adams_terceira, Adams_quarta 
import leitura,time
import sys


arq = sys.argv[ 1 ]
l = leitura.ler( arq )

v0 = l[ 0 ]#recebe o valor de v0
i = l[ 1 ]#recebe o numero da funcao escolhida
h = l[ 2 ]#recebe o valor de h
t0 = l[ 3 ][ 0 ] #recebe o limite inferior
tn = l[ 3 ][ 1 ] #recebe o limite superior
n = 5 #quantidade de linhas que a tabela vai ter

print "figure;"

if ( i == 1 ): 
	print 'a = ezplot("e^( 0.25 * t^4 - 1.5 * t  )",[ 0 , 2 ])' 
elif ( i == 2 ):
	print 'a = ezplot( "(1 / 4) * ( 2 * t^2 + t + 2 )^2",[ 0 , 1 ])'
elif ( i == 3 ):
	print 'a = ezplot("(1 / 4) * ( 2 * t^2 - 2 * t + 3 * e^ (-2 * t) + 1 )",[ 0 , 2 ])'
else :
	print 'funcao fora do intervalo' 


print 'set(a,"linewidth",2)'
print 'set(a,"color","k")'
print 'grid on'
print 'hold on'


#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )

print ( 'teuler = ' ), tempo
#imprimindo o vetor com valores da velocidade	

velocidade = euler( f, i, v0, tempo, h,  )
print ( 'yeuler = ' ), velocidade

print 'euler = plot( teuler, yeuler )'
print 'set(euler,"linewidth",2)'
print 'set(euler,"color","b")'
print 'hold on'

#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )

#imprimindo o vetor com valores da velocidade
velocidade = RungeKutta_segunda( f, i, v0, tempo, h )
print ( 'trk2 = ' ), tempo
print ( 'yrk2 = ' ), velocidade

print 'rk2 = plot(trk2, yrk2, "-r")'
print 'set(rk2,"linewidth",2)'
print 'hold on'	

#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )

#imprimindo o vetor com valores da velocidade	
velocidade = RungeKutta_terceira( f, i, v0, tempo, h )

print ( 'trk3 = ' ), tempo
print ( 'yrk3 = ' ), velocidade

print 'rk3 = plot(trk3, yrk3, "-g")'
print 'set(rk3, "linewidth", 2)'
print 'hold on'	

#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )
#imprimindo o vetor com valores da velocidade	
velocidade = RungeKutta_quarta( f, i, v0, tempo, h )
print ( 'trk4 =' ), tempo
print ( 'yrk4 =' ), velocidade

print 'rk4 = plot(trk4, yrk4, "-c")'
print 'set(rk4, "linewidth", 2)'
print 'hold on'	


#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )
#imprimindo o vetor com valores da velocidade	
velocidade = Adams_terceira( f, i, tempo, h, v0 )
print ('tada3 = '), tempo
print ('yada3 = '), velocidade

print 'ada3 = plot(tada3, yada3, "-m")'
print 'set(ada3, "linewidth", 2)'
print 'hold on'	
	
#imprimindo o vetor com valores do tempo	
tempo = t( t0, tn, n )
#imprimindo o vetor com valores da velocidade	
velocidade = Adams_quarta( f, i, tempo, h, v0)
print ('tada4 = '), tempo
print ('yada4 = '), velocidade

print 'ada4 = plot(tada4, yada4, "-k")'
print 'set(ada4, "linewidth", 1)'
print 'hold on'	
print "legend('solucao analitica','Forward Euler', 'RK2', 'RK3','RK4', 'ADA3', 'ADA4');"
