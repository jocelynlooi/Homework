#比数楼梯多了一个条件，不一定是1/2步
dp = [0] * (int(input()) + 1)
dp[0] = 1
for i in range(1, len(dp)):
    dp[i] = sum(dp[:i])
print(dp[-1])
