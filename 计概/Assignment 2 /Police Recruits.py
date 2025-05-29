n= int(input())
a= list(map(int,input().split()))
case=0
officers=0
for i in a:
    if i == -1 and officers==0:
        case+=1
        continue
    elif i>0:
        officers+=i
        continue
    officers-=1

print(case)
