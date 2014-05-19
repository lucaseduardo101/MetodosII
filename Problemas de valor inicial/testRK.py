import sys
import math
import time
ini = time.time()

arquivo = open(str(sys.argv[1]), "r")
listaStr = arquivo.readlines()
tamanhoLista = len(listaStr)
tamanhoLista = int(tamanhoLista)
arquivo.close()

_x0 = float(listaStr[0].split()[0])
_indf = int(listaStr[1].split()[0])
_h = float(listaStr[2].split()[0])
_t0 = float(listaStr[tamanhoLista-1].split()[0])
_tn = float(listaStr[tamanhoLista-1].split()[1])

_tam = int((_tn-_t0)/_h) + 1
_t = range(_tam)
_flag = _t0

for i in xrange(_tam):
	_t[i] = _flag
	_flag = _flag + _h
	
print "\nx0 =", _x0
print "\nindf =", _indf
print "\nh =", _h
print "\nt0 =", _t0
print "\ntn =", _tn
print "\nt =", _t


#-----------------------------------------------------------------------------

def f(x, t, indf):
	if indf == 1:
		return x*(t**3) -1.5*x
	elif indf == 2:
	    return (1+(4*t))*math.sqrt(x)
	elif indf == 3:
		return -2*x + t*t	
		
#-----------------------------------------------------------------------------

def rk2(f, indf, x0, t, h):
	n = len(t)
	x = range(n)
	x[0] = x0
	for i in xrange(n - 1):
		k1 = h * f( x[i], t[i], indf )
		print k1,"k1"
		k2 = h * f( x[i] + k1, t[i+1], indf )
		print k2,"k2"
		x[i+1] = x[i] + ( k1 + k2 ) / 2.0
	return x

#-----------------------------------------------------------------------------

def rk3(f, indf, x0, t, h):
	n = len(t)
	x = range(n)
	x[0] = x0
	for i in xrange(n - 1):
		k1 = h * f( x[i], t[i], indf )
		k2 = h * f( x[i] + k1/2.0, t[i] + h/2.0, indf )
		k3 = h * f( x[i] - k1 + 2.0*k2, t[i] + h, indf )
		x[i+1] = x[i] + ( k1 + 4.0*k2 +k3 ) / 6.0
	return x

#-----------------------------------------------------------------------------

def rk4(f, indf, x0, t, h):
	n = len( t )
	x = range(n)
	x[0] = x0
	for i in xrange( n - 1 ):
		k1 = h * f( x[i], t[i], indf )
		k2 = h * f( x[i] + k1/3.0, t[i] + h/3.0, indf )
		k3 = h * f( x[i] + k1/3.0 + k2/3.0, t[i] + (2.0*h)/3.0, indf )
		k4 = h * f( x[i] + k1 - k2 + k3, t[i] + h, indf )
		x[i+1] = x[i] + ( k1 + 3.0*k2 + 3.0*k3 + k4 ) / 8.0
	return x

#-----------------------------------------------------------------------------

_rk2 = rk2( f, _indf, _x0, _t, _h )
_rk3 = rk3( f, _indf, _x0, _t, _h )
_rk4 = rk4( f, _indf, _x0, _t, _h )

fim = time.time()
temp = fim-ini
print "\nrk2 -> x =",_rk2
print "\nrk3 -> x =",_rk3
print "\nrk4 -> x =",_rk4
print "\nTempo: ",temp
