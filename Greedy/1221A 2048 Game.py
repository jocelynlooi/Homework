q = int(input())
ans=[]
for i in range (q):
    n= int(input())
    s= [x for x in map(int,input().split())if x<2049]
    win= sum(s)>= 2048
    if win: ans.append('YES')
    else: ans.append('NO')
for a in ans :print(a)
