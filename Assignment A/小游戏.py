from collections import deque


def bfs(start, end, grid, h, w):
    queue = deque([start])
    visited = set()
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    ans = []
    while queue:
        x, y, d_i_r, seg = queue.popleft()
        # print(x,y,end)
        if (x, y) == end:
            # return seg
            ans.append(seg)
            break

        for i, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy

            if 0 <= nx < h + 2 and 0 <= ny < w + 2 and ((nx, ny, i) not in visited):
                new_dir = i
                new_seg = seg if new_dir == d_i_r else seg + 1
                if (nx, ny) == end:
                    # return new_seg
                    ans.append(new_seg)
                    continue

                if grid[nx][ny] != 'X':
                    visited.add((nx, ny, i))
                    queue.append((nx, ny, new_dir, new_seg))

    if len(ans) == 0:
        return -1
    else:
        return min(ans)


board_num = 1
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    # grid = [[' '] * (w + 2)] + \
    # [[' '] + list(input()) + [' '] for _ in range(h)] + \
    # [[' '] * (w + 2)]
    grid = [' ' * (w + 2)] + [' ' + input() + ' ' for _ in range(h)] + [' ' * (w + 2)]
    print(f"Board #{board_num}:")
    pair_num = 1
    while True:
        y1, x1, y2, x2 = map(int, input().split())
        if x1 == y1 == x2 == y2 == 0:
            break

        start = (x1, y1, -1, 0)
        end = (x2, y2)

        seg = bfs(start, end, grid, h, w)
        if seg == -1:
            print(f"Pair {pair_num}: impossible.")
        else:
            print(f"Pair {pair_num}: {seg} segments.")
        pair_num += 1

    print()
    board_num += 1