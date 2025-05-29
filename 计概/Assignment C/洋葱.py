def dfs(n, s, x, y):
    if n == 1:
        return s[x][y]
    if n == 0:
        return 0
    curr = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(4 * (n - 1)):
        dx, dy = directions[(i // (n - 1)) % 4]
        x += dx
        y += dy
        curr += s[x][y]
    return max(curr, dfs(n - 2, s, x + 1, y + 1))


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

result = dfs(n, s, 0, 0)
print(result)