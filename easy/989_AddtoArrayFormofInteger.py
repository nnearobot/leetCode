# 989. Add to Array-Form of Integer
# Easy
# https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        kArr = []
        while k > 0:
            kArr.append(k % 10)
            k = k // 10
        numL = len(num)
        kArrL = len(kArr)
        n = max(numL, kArrL)
        res = []
        carry = 0
        for i in range(n):
            el1 = kArr[i] if i < kArrL else 0
            el2 = num[numL - i - 1] if i < numL else 0
            summ = el1 + el2 + carry
            carry = summ // 10
            summ = summ % 10
            res.insert(0, summ)
        
        if carry:
            res.insert(0, carry)

        return res