
import itertools

inf=10**9
n,m=map(int,input().split())
p=[[inf]*m for _ in range(n)]
q=[[] for _ in range(m)]
for i in range(n):
    *sold,=input().split()
    for s in sold:
        si=int(s[0])-1
        pi=int(s[2:])
        p[i][si]=pi
for j in range(m):
    *quan,=input().split()
    for s in quan:
        a,b=map(int,s.split('-'))
        q[j].append([a,b])
plans=itertools.product(range(m),repeat=n)
final_money=inf
for plan in plans:
    money=[0]*m
    for i in range(n):
        money[plan[i]]+= p[i][plan[i]]
    final=sum(money)
    final-=final//300*50
    for j in range(m):
        maxq=0
        for qq in q[j]:
            if money[j]>=qq[0]:
                maxq=max(qq[1],maxq)
        final-=maxq
    if final<final_money:
        final_money=final
print(final_money)