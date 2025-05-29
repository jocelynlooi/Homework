import sys

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(matrix, x, y, target_x, target_y):
    m, n = len(matrix), len(matrix[0])
    h = matrix[x][y]
    stack = [(x, y)]
    visited = [[False for _ in range(n)] for _ in range(m)]

    while stack:
        x, y = stack.pop()
        if x == target_x and y == target_y:
            return True
        visited[x][y] = True
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:  # 确保新坐标在矩阵范围内
                if not visited[nx][ny] and matrix[nx][ny] < h:  # 允许流向等高或更低的位置
                    stack.append((nx, ny))

    return False


# 读取并处理输入
data = sys.stdin.read().split()
k = int(data[0])
id = 1
ans = []

for _ in range(k):
    m, n = int(data[id]), int(data[id + 1])
    id += 2
    matrix = [list(map(int, data[id + i * n:id + (i + 1) * n])) for i in range(m)]
    id += m * n
    a, b = int(data[id]) - 1, int(data[id + 1]) - 1
    id += 2
    p = int(data[id])
    id += 1
    pos = [(int(data[id + i * 2]) - 1, int(data[id + i * 2 + 1]) - 1) for i in range(p)]
    id += p * 2

    result = any(dfs(matrix, x, y, a, b) for x, y in pos)
    ans.append("Yes" if result else "No")

sys.stdout.write("\n".join(ans) + "\n")