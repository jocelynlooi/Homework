n = int(input())
t = [(i, int(j)) for i, j in enumerate(input().split(), 1)]
tt = t.copy()
tt.sort(key=lambda x: x[1])
ans = []
for i in tt:
    ans.append(i[0])
print(*ans)
dp = [0] * n
dp[0] = 0
for i in range(1, n):
    dp[i] = dp[i - 1] + tt[i - 1][1]

print('{:.2f}'.format(sum(dp) / n))