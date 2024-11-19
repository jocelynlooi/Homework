ans=0
n, m = map(int,input().split())
edge = [0]*(m+2)
imap = [edge,*[[0,*[*map(int,input().split())],0]for _ in range(n)], edge]
for r in range(1, n+1):
    for c in range(1, m+1):
        if imap[r][c]:
            ans += 4 -imap[r-1][c] -imap[r+1][c] -imap[r][c-1] -imap[r][c-1]
print(ans)