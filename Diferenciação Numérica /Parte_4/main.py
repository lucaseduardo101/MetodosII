from extraRichard import extraRichard
import leitura2
import sys

arq = sys.argv[1]
l = leitura2.ler(arq)


i=l[0]#recebe o numero da funcao escolhida
h=l[1]#recebe o valor de h -obs: vai ser uma posicao do vetor simples,ajeitar isso
x=l[2]#recebe o valor de x onde a funcao deve ser diferenciada -obs:ajeitar isso

h1 = 0.5
i = 1
x = 0.5

extraRichard(h1, i, x)
