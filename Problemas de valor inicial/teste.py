import init


	
print ('\n-------------Metodo RungeKutta_terceira ordem-------------')
#imprimindo o vetor com valores do tempo	
tempo= [0,0.2,0.4,0.6]
#imprimindo o vetor com valores da velocidade	

velocidade = init.RungeKutta_quarta(1,0,tempo,0.5,1.0)

print ('valores coluna tempo:'),tempo
print ('valores coluna velocidade:'),velocidade

