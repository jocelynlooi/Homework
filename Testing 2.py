def f(n) :
    if n <= 2:
        return 1
    else:
        return f(n-1) + f(n-2)

n = int(input())
ans = []
for _ in range(n):
    num = int(input())
    ans.append(f(num))

print('\n'.join(map(str, ans)))