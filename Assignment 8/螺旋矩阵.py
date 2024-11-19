n = int(input())
edge = [[1]*(n+2)]
mx = edge + [[1,*[0]*n, 1] for _ in range(n)] + edge
turn = [(0, 1), (1, 0), (0,-1), (-1, 0)]
y = x = 1 ; t=0
dy, dx = turn[t]
for num in range(1, n**2 +1):
    mx[y][x] = num
    if mx[y+dy][x+dx]:
        t = (t+1)%4
        dy, dx = turn[t]
    y += dy
    x += dx
for row in mx[1:-1]: print(*row[1:-1])