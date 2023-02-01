# 1017. Convert to Base -2
# Medium
# https://leetcode.com/problems/convert-to-base-2/description/

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = ""
        while n:
            rem = n % -2
            n //= -2
            if rem == -1:
                n += 1
            res = str(abs(rem)) + res
        return res