import math
n,m,a =[int(x) for x in input().split()]
p= math.ceil(n/a)
q= math.ceil(m/a)
print(p*q)

