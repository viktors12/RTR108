#print vars() #for python2

#print (vars())
a=10
#print("%s"%(vars()))

import math as math
print(math.cos(a))

import math as math_V1
print(math_V1.cos(a))

from math import cos as cos_V1
print(cos_V1(a))

from cmath import cos as cos_V2
print(cos_V2(a))

from math import *
print(cos(a))
