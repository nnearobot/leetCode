# 1143. Longest Common Subsequence
# medium
# https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for l1 in range(n1):
            for l2 in range(n2):
                i, j = l1 + 1, l2 + 1
                if text1[l1] == text2[l2]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n1][n2]
        
'''
dp:
   abc
  0000 
k 0000
l 0000
b 0011
f 0011
c 0012

'''