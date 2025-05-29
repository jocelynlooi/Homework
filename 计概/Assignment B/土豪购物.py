def max_profit(vals):
    n = len(vals)
    if n == 1:
        return vals[0]

    max_sum = left = vals[0]
    for i in range(1, n):
        left = max(vals[i], left+vals[i])
        max_sum = max(max_sum, left)

    left_max = [0]*n
    left_max[0] = vals[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1]+ vals[i], vals[i])

    right_max = [0] * n
    right_max[n-1] = vals[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(vals[i], right_max[i+1] + vals[i])

    max_removed = float('-inf')
    for i in range(1, n-1):
        max_removed = max(max_removed, left_max[i-1]+right_max[i+1])

    max_removed = max(max_removed, right_max[1], left_max[n-2])

    return max(max_sum, max_removed)

def main():
    vals = list(map(int,input().split(',')))
    print(max_profit(vals))

if __name__ == "__main__":
    main()