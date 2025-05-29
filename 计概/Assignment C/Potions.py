a=int(input())
potions=list(map(int,input().split()))
dp=[-float('inf')]*(1+a)
dp[0]=0
for i in range(1+a):
	for j in range(i,0,-1):
		temp=max(dp[j],dp[j-1]+potions[i-1])
		if temp>=0:
			dp[j]=temp
for i in range(a,-1,-1):
	if dp[i]>=0:
		print(i)
		break