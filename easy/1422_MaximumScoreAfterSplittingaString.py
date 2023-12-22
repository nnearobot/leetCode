# 1422. Maximum Score After Splitting a String
# easy
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        score = s.count("1")
        score += 1 if s[0] == "0" else -1
        max_score = score
        for i in range(1, len(s) - 1):
            score += (-1 if s[i] == "1" else 1)
            max_score = max(score, max_score)

        return max_score