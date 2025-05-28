from collections import deque, defaultdict
from typing import List


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        portal_map = defaultdict(list)
        for i in range(m):
            for j in range(n):
                c = matrix[i][j]
                if 'A' <= c <= 'Z':
                    portal_map[c].append((i, j))

        INF = 10 ** 18
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0

        dq = deque()
        dq.append((0, 0))

        while dq:
            x, y = dq.popleft()
            d = dist[x][y]
            if x == m - 1 and y == n - 1:
                return d

            c = matrix[x][y]
            if 'A' <= c <= 'Z' and portal_map[c]:
                for px, py in portal_map[c]:
                    if dist[px][py] > d:
                        dist[px][py] = d
                        dq.appendleft((px, py))
                portal_map[c].clear()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m and 0 <= ny < n
                        and matrix[nx][ny] != '#'
                        and dist[nx][ny] > d + 1):
                    dist[nx][ny] = d + 1
                    dq.append((nx, ny))

        return -1
