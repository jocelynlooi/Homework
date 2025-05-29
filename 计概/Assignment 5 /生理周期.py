num = 1
while True:
    p, e, i, d = map(int, input().split())
    if [p, e, i, d] == [-1, -1, -1, -1]:
        break
    s = d + 1
    while (s - p) % 23 != 0 or (s - e) % 28 != 0 or (s - i) % 33 != 0:
        s += 1
    s -= d
    print(f'Case {num}: the next triple peak occurs in {s} days.')
    num += 1