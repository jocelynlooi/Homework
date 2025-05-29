d = int(input())
n = int(input())
base= [[0] * 1025 for _ in range(1025)]
for _ in range(n):
    x, y, k = map(int, input().split())
    for i in range(max(0, x - d), min(1025, x + d + 1)):
        for j in range(max(0, y - d), min(1025, y + d + 1)):
            base[i][j] += k
maximum = max(max(l) for l in base)
num = sum(l.count(maximum) for l in base)
print(num, maximum)