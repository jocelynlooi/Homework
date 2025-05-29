def is_blessed_id(A):
    squares = set()
    i = 1
    while i * i <= 10 ** 9: #平方up to 10^9 stored
        squares.add(i * i)
        i += 1

    digits = list(map(int, str(A))) #split every digit

    def dfs(idx):
        if idx == len(digits):
            return True

        num = 0
        for i in range(idx, len(digits)):
            num = num * 10 + digits[i] #add 1 digit to num
            if num in squares:
                if dfs(i + 1):
                    return True
        return False


    return "Yes" if dfs(0) else "No"



A = int(input())
print(is_blessed_id(A))