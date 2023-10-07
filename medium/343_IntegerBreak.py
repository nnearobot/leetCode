# 343. Integer Break
# Medium
# https://leetcode.com/problems/integer-break/description

class Solution:
    def integerBreak(self, n: int) -> int:
        maxProduct = 0
        count = 2
        while count <= n:
            mult = n // count
            mod = n % count
            prod = 1
            for i in range(count):
                multiplicator = mult if i < count - mod else mult + 1
                prod *= multiplicator
            if prod > maxProduct:
                maxProduct = prod
            count += 1
        return maxProduct