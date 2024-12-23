rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

points = sorted([(matrix[i][j], i, j) for i in range(rows) for j in range(cols)])

dp = [[1] * cols for _ in range(rows)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

longest_path = 1

for height, x, y in points:
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] < height:
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
    longest_path = max(longest_path, dp[x][y])

print(longest_path)
