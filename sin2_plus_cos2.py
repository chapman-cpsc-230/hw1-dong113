
from math import sin, cos, pi
x = pi/4
val = sin(x)**2 + cos(x)**2
print(val),"\n"



vi = 3
t = 1
a = 2
s = vi*t + .5*a*t**2  #3+1
print (s), "\n"



a = 3.3 ; b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print "First equation: %d = %d" % (eq1_sum, eq1_pow)
print "Second equation: %d = %d" % (eq2_pow, eq2_pow)


