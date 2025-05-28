grade = [float(x) for x in input().split()]
le = len(grade)
grade.sort()
targ = grade[int(le * 0.4)]
left = 0
right = 1000000000
while left <= right:
    mid = (left + right) // 2
    gd = targ * mid / 1000000000 + 1.1 ** (targ * mid / 1000000000)
    if gd >= 85:
        right = mid - 1
    else:
        left = mid + 1
print(left)
