# 1688. Count of Matches in Tournament
# easy
# https://leetcode.com/problems/count-of-matches-in-tournament

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1

        matches = 0
        while n > 1:
            if n % 2 == 1:
                matches += (n - 1) // 2
                n = n // 2 + 1
            else:
                n = n // 2
                matches += n
        return matches
