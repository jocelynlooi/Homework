while True:
    try:
        s = input().strip()
    except EOFError:
        break

    if s.count('@') != 1:
        print("NO")
        continue

    if s[0] in {'@', '.'} or s[-1] in {'@', '.'}:
        print("NO")
        continue

    if "@." in s or ".@" in s:
        print("NO")
        continue

    p = s.find("@")
    q = s.find(".", p + 1)

    if q == -1 or q == len(s) - 1:
        print("NO")
        continue

    if p == 0 or q == p + 1:
        print("NO")
        continue

    if ".." in s:
        print("NO")
        continue

    print("YES")
