# 977. Squares of a Sorted Array
# Easy
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack = []
        res = []
        for n in nums:
            sqr = n * n
            if n < 0:
                stack.append(sqr)
            else:
                while (len(stack) > 0 and stack[len(stack) - 1] <= sqr):
                    res.append(stack.pop())
                res.append(sqr)
        if len(stack) > 0:
            for i in range(len(stack) - 1, -1, -1):
                res.append(stack[i])
        
        return res
