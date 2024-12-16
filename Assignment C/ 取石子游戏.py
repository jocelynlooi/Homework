def dfs(a, b):
    if a // b >= 2 or a == b:
        return True
    else:
        return not dfs(b, a - b)


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if b > a:
        a, b = b, a
    if dfs(a, b):
        print("win")
    else:
        print("lose")