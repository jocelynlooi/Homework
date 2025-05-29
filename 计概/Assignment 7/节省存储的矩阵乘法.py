n,m1,m2 = map(int,input().split())
a=[[0]* n for _ in range (n)]
b=[[0]* n for _ in range (n)]
for _ in range(m1):
    x,y,v = map(int,input().split())
    a[x][y]= v
for _ in range(m2):
    x,y,v = map(int,input().split())
    b[x][y]= v
c= [[0]* n for _ in range (n)]
for i in range(n):
    for j in range(n):
        c[i][j]= sum(a[i][k]*b[k][j] for k in range(n))
        if c[i][j] != 0:
            print (i,j,c[i][j])
