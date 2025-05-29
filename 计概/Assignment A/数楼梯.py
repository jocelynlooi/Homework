#可以1/2阶,+1&+2until get input num
n= int(input())

a=1
b=1
n-=1

if n>0:
    while n>0:
        c=a+b #c=sum
        a=b
        b=c
        n-=1
    print(b)

elif n==0: #直到n=0
    print(a)



