def dfs(x, y, now_value):
    global max_value, opt_path
    if x == n - 1 and y == m - 1:
        if now_value > max_value:
            max_value = now_value #找最大值，一直更新
            opt_path = temp_path[:]
        return

    visited[x][y] = True #已访问

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
            next_value = now_value + maze[next_x][next_y]
            temp_path.append((next_x, next_y))
            dfs(next_x, next_y, next_value)
            temp_path.pop()


    visited[x][y] = False

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

max_value = float('-inf') # 先设max value为一个很小的数
opt_path = []
temp_path = [(0, 0)]
visited = [[False] * m for _ in range(n)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


dfs(0, 0, maze[0][0])


for x, y in opt_path:
    print(x + 1, y + 1)