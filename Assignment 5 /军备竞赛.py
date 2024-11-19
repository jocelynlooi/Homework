p = int(input())
cost = sorted(list(map(int, input().split())))
i, j, cnt = 0, len(cost) - 1, 0
while i < j:
    if cost[i] <= p:
        cnt += 1
        p -= cost[i]
        i += 1
    elif cnt:
        cnt -= 1
        p += cost[j]
        j -= 1
    else:
        break

print(cnt + (cost[i] <= p))