# 5. Longest Palindromic Substring
# Medium
# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(i, j):
            while True:
                if i < 1 or j > len(s) - 2:
                    break
                if s[i - 1] != s[j + 1]:
                    break
                i -= 1
                j += 1
            return (i, j)

        maxLength = 0
        answer = ""
        for center in range(len(s)):
            for (i, j) in [(center, center), (center, center + 1)]:
                if j >= len(s) or s[i] != s[j]:
                    continue
                (minP, maxP) = getPalindrome(i, j)
                if (maxP - minP + 1) > maxLength:
                    answer = s[minP:maxP + 1]
                    maxLength = len(answer)
        
        return answer
            