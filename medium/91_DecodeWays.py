# 91. Decode Ways
# medium
# https://leetcode.com/problems/decode-ways/description

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        # bottom-top dynamic programming:
        #return self.dp(s)

        # backtracking with memoization:
        self.memo = [[-1, -1] for _ in range(len(s))] # L, xL
        return self.backTrack(s, 0, 0)
    
    def dp(self, s) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(dp)):
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
            
            if s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
    
    def backTrack(self, s: str, i: int, i_start: int) -> int:
        length = i_start - i

        if length == 0:
            if s[i] == "0":
                return 0
        else:
            if length > 2:
                return 0
            else:
                if int(s[i_start : i + 1]) > 26:
                    return 0

        if i == len(s) - 1:
            return 1
        
        # take current letter, if it is possible:
        if self.memo[i][0] == -1:
            self.memo[i][0] = self.backTrack(s, i + 1, i + 1)
        res = self.memo[i][0]

        # not take current letter - try with next letter, if it is possible:
        if i_start == i:
            if self.memo[i][1] == -1:
                self.memo[i][1] = self.backTrack(s, i + 1, i_start)
            res += self.memo[i][1]

        return res
