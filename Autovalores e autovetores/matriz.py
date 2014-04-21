#para ciar uma matriz vazia

def criaMatriz(n,m):
	mat= [0]*n
	for i in range(n):
		mat[i]=[0]*m
	return mat

#criar matriz identidade de tamanho n
def criaMatrizIdent(n):
	mat=criaMatriz(n,n)
	for i in range(n):
		mat[i][i]=1
	return mat

#imprimir a matriz
def mostraMatriz(mat,n):
	for i in range(n):
		print mat[i][:]
	print '\n'

#para criar uma segunda matriz que e o dobro da primeira
def mult_escalar1(mat,a,n):
	mat2=criaMatriz(n,n)
	for i in range(n):
		for j in range(n):
			mat2[i][j]=mat[i][j]*a
	return mat2

#soma duas matrizes do mesmo tamanho
def somar(m1, m2):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos tem em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo indice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma
 
 
def mult_escalar(matriz, escalar):
    matriz_mult = []
    quant_linhas = len(matriz) # Conta quantas linhas existem
    quant_colunas = len(matriz[0]) # Conta quantos elementos tem em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_mult
        matriz_mult.append([])
        for j in range(quant_colunas):
            # Multiplicando cada elemento pelo escalar
            mult = escalar * matriz[i][j]
            matriz_mult[i].append(mult)
    return matriz_mult

#como preencher a matriz com dados
matrizTeste =[[51,81],[9,14]]

#testando somar matrizes
matrizTeste1=[[51,81],[9,14]]
mostraMatriz(matrizTeste1,2)

matrizTeste2=[[2,-3],[-1,2]]
mostraMatriz(matrizTeste2,2)

somaTeste=somar(matrizTeste1,matrizTeste2)

mostraMatriz(somaTeste,2)

#trabalhando com matriz identidade ex:2x2
n=input('Dimenssao da matriz: ')
mat1=criaMatrizIdent(n)
mat2=criaMatriz(n,n)
mat3=mult_escalar(matrizTeste1,2)

mostraMatriz(mat1,n)
mostraMatriz(mat2,n)
mostraMatriz(mat3,n)
