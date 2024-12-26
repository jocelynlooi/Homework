n = int(input())
num= 0
for _ in  range(n):
    a,b,c=[int(x) for x in input().split()]
    if a+b+c>1:
        num+=1
print(num)
