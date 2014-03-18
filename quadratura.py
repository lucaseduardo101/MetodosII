#teste para quadratura gausiana para n=1

def x(t):
	return ((b-a)/2)*t + (a+b)/2

def f(x):
	return (2*x**3 + 3*x**2 + 6*x+1)

print "f(x1)=",f(1.8452)

print "f(x2)=",f(4.1548)

b=5
a=1
A0=1
A1=1

def x(t):
	return ((b-a)/2)*t + (a+b)/2

t1=-0.5774
t2=0.5774
x1=x(t1)
x2=x(t2)

def quadGaussianna(a,b,A0,A1,x1,x2):
	return ((b-a)/2) * (A0*f(x1)+A1*f(x2))

print "valor da integral=" ,quadGaussianna(a,b,A0,A1,x1,x2)
