class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 1
        s_x, s_y = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j, -1,-1):
                if j - i >= 2:
                    # 当3个以上
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j]
                if dp[i][j] and j - i + 1 > ans:

                    ans = j - i + 1
                    s_x, s_y = i, j
        return s[s_x : s_y + 1]