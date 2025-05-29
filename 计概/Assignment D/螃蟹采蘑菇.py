from collections import deque


dire = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(a, x1, y1, x2, y2):
    visit = set()
    queue = deque([(x1, y1, x2, y2)])
    visit.add((x1, y1, x2, y2))

    while queue:
        xa, ya, xb, yb = queue.popleft()
        for xi, yi in dire:
            nx1, ny1 = xa + xi, ya + yi
            nx2, ny2 = xb + xi, yb + yi

            if 0 <= nx1 < a and 0 <= ny1 < a and 0 <= nx2 < a and 0 <= ny2 < a:
                if (nx1, ny1, nx2, ny2) not in visit and Matrix[nx1][ny1] != 1 and Matrix[nx2][ny2] != 1:
                    queue.append((nx1, ny1, nx2, ny2))
                    visit.add((nx1, ny1, nx2, ny2))
                    if Matrix[nx1][ny1] == 9 or Matrix[nx2][ny2] == 9:
                        return True
    return False

a = int(input())
Matrix = [list(map(int, input().split())) for _ in range(a)]

x1, y1, x2, y2 = -1, -1, -1, -1
found_first = False

for i in range(a):
    for j in range(a):
        if Matrix[i][j] == 5:
            if not found_first:
                x1, y1 = i, j
                Matrix[i][j] = 0
                found_first = True
            else:
                x2, y2 = i, j
                Matrix[i][j] = 0
                break
    if x2 != -1:
        break

check = bfs(a, x1, y1, x2, y2)
print('yes' if check else 'no')
