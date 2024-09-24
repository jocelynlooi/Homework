import math
n,m,a= [int(x) for x in input().split()]
l= math.ceil(n/a)
w= math.ceil(m/a)
print (l*w)
