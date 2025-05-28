def find_closest_sum(T, numbers):
    numbers_sorted = sorted(numbers)
    left = 0
    right = len(numbers_sorted) - 1
    closest_sum = None
    min_diff = float('inf')

    while left < right:
        current_sum = numbers_sorted[left] + numbers_sorted[right]
        current_diff = abs(current_sum - T)

        if current_diff < min_diff:
            min_diff = current_diff
            closest_sum = current_sum
        elif current_diff == min_diff:
            if current_sum < closest_sum:
                closest_sum = current_sum

        if current_sum < T:
            left += 1
        elif current_sum > T:
            right -= 1
        else:
            return current_sum

    return closest_sum


T = int(input())
numbers = list(map(int, input().split()))
print(find_closest_sum(T, numbers))
