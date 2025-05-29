def f(string):
    if string=='':
        return 0
    else:
        return int(string)
m=int(input())
n=int(input())
l=input().split()
for i in range(n):
    for j in range(n-1-i):
        if l[j] + l[j+1] > l[j+1] + l[j]:
            l[j],l[j+1] = l[j+1],l[j]
weight=[]
for num in l:
    weight.append(len(num))
dp=[['']*(m+1) for _ in range(n+1)]
for k in range(m+1):
    dp[0][k]=''
for q in range(n+1):
    dp[q][0]=''
for i in range(1,n+1):
    for j in range(1,m+1):
        if weight[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
                dp[i][j]=str(max(f(dp[i-1][j]),int(l[i-1]+dp[i-1][j-weight[i-1]])))
print(dp[n][m])