
input()
*a, = map(int, input().split())
x = max(a)
an = [0]*(x+1)
for i in a:
    an[i] += 1
dp = [0]*(x+1)
for j in range(1,x+1):
    dp[j] = max(dp[j-1], dp[j-2] + an[j]*j)
print(dp[-1])