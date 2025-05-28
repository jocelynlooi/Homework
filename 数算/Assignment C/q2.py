def count_stack_sequences(n):
    def backtrack(open_count, close_count):
        if open_count == n and close_count == n:
            return 1
        total_count = 0
        if open_count < n:
            total_count += backtrack(open_count + 1, close_count)
        if close_count < open_count:
            total_count += backtrack(open_count, close_count + 1)
        return total_count

    return backtrack(0, 0)

if __name__ == "__main__":
    n = int(input())
    result = count_stack_sequences(n)
    print(result)
