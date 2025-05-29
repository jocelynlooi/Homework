def wiggleMaxLength(nums) :
    n =  len(nums)
    if n == 1:
        return 1

    direction = None

    res = 0

    for i in range(1,n):
        if nums[i] == nums[i-1]:
            continue

        elif nums[i] > nums[i-1]:
            if direction == 1:
                continue
            direction = 1
            res += 1

        else:
            if direction == 0:
                continue
            direction = 0
            res += 1

    return res+1

input ()
*nums, = map(int, input().split())
print(wiggleMaxLength(nums))