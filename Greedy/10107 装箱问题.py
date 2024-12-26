extra=[0,5,3,1]
while 1:
    a,b,c,d,e,f= list(map(int, input().split()))
    if a+b+c+d+e+f==0:
        break
    box= f+e+d-(-c//4)
    can_b= 5*d+extra[c%4]

