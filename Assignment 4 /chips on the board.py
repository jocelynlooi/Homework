t = int(input())
for _ in range(t):
    n = int(input())
    *a, = map(int, input().split())
    *b, = map(int, input().split())

    min_a = min(a)
    min_b = min(b)

    ans1 = sum([min_a + i for i in b])
    ans2 = sum([min_b + i for i in a])
    print(min(ans1, ans2))