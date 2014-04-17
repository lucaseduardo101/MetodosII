from math import sqrt, exp, sin, cos


#os dados abaixo sao as entradas dadas pelo arquivo

n=3 #numero de pontos fornecidos
x0=0
x1=1.04
x2=1.75
x=1.5#valor onde a funcao vai ser referenciada

fx0=153
fx1=208
fx2=249

#criei esses auxs para nao dar problema na formula
aux1=x0-x1
print ("x0-x1= "),aux1

aux2=x0-x2
print ("x0-x2= "),aux2

aux3=x1-x0
print ("x1-x0= "),aux3

aux4=x1-x2
print ("x1-x2= "),aux4

aux5=x2-x0
print ("x2-x0= "),aux5

aux6=x2-x1
print ("x2-x1= "),aux6

aux7=2*x
print ("2*x= "),aux7

#aqui vai calcular o valor da primeira derivada no ponto x,que e a saida

primeiraDerivada= ((fx0)*((aux7-x1-x2)/(aux1*aux2))) + ((fx1)*((aux7-x0-x2)/(aux3*aux4))) + ((fx2)*((aux7-x0-x1)/(aux5*aux6))) 

print ("Primeira Derivada= "),primeiraDerivada


