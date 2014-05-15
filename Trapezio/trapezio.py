#metodos para trapezio sem  repeticao
f=[]
def h_simples(xm,x0):
	return(xm-x0)

def trapezioSimples(h,fx0,fx1):
	return ((h/2)*(fx0+fx1))

def erro(integral,it):
	return (integral-it)

#metodos para trapezio com repeticao

def h_repetido(b,a,m):
	aux=(float)(b-a)
	h2=aux/m
	return h2

def trapezioRepetido(h,fx0,fx1,somatorio):
	return ((h/2)*(fx0+(2*somatorio)+fx1))

def somatorio(f,m):
	s=0
	#Realiza o somatorio
	for i in range(1,m):
		print "f[ ",i,"] =", f[i]
		s = s + f[i]
	return s
