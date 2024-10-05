n= int(input())
a=list(map(int,input().split()))
cnt=0
officers=0
for i in a:
    if i== -1 and officers==0:
        cnt+=1
        continue
    if i>0:
        officers+=i
        continue
    officers-=1

print(cnt)


