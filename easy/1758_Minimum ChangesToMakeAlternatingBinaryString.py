# 1758. Minimum Changes To Make Alternating Binary String
# easy
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

class Solution:
    def minOperations(self, s: str) -> int:
        even, odd = 0, 0
        for i, l in enumerate(s):
            if i % 2 == 0:
                if l == "1":
                    odd += 1
                else:
                    even += 1
            else:
                if l == "0":
                    odd += 1
                else:
                    even += 1
        return min(odd, even)