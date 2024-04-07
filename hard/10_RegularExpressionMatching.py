# 10. Regular Expression Matching
# hard
# https://leetcode.com/problems/regular-expression-matching/description/

class Solution:
    # Dynamic programming bottom-up solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                is_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or is_match and dp[i + 1][j]
                else:
                    dp[i][j] = is_match and dp[i + 1][j + 1]

        return dp[0][0]
    
    
    
    '''
    # Dynamic programming top-bottom solution:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    res = i == len(s)
                else:
                    is_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                    if j + 1 < len(p) and p[j + 1] == '*':
                        res = dp(i, j + 2) or is_match and dp(i + 1, j)
                    else:
                        res = is_match and dp(i + 1, j + 1)
                memo[i, j] = res
            return memo[i, j]

        return dp(0, 0)
    '''


    '''
    # Recursive solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        is_match = len(s) > 0 and (p[0] == s[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return (is_match and self.isMatch(s[1:], p) or self.isMatch(s, p[2:]))
        else:
            return is_match and self.isMatch(s[1:], p[1:])
    '''
