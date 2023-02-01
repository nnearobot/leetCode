# 504. Base 7
# Easy
# https://leetcode.com/problems/base-7

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = ""
        isNeg = num < 0
        while num:
            rem = abs(num) % 7
            num = abs(num) // 7
            res = str(rem) + res
            print(res, num)
        return "-" + res if isNeg else res