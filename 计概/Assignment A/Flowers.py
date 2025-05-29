# rule: white in size k
t,k=map(int,input().split())
dp=list([0]*2 for _ in range(100001))
p=[0]*(100001)
dp[0][0]=1
dp[0][1]=0
p[0]=1


for i in range(1,100001):
    dp[i][0]=(dp[i-1][0]+dp[i-1][1])%1000000007
    if i>=k:
       dp[i][1]=(dp[i-k][0]+dp[i-k][1])%1000000007
    p[i]=(p[i-1]+dp[i][0]+dp[i][1])%1000000007
for _ in range(t):
    a,b=map(int,input().split())
    print((p[b]-p[a-1])%1000000007)