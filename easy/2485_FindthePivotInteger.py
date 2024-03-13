# 2485. Find the Pivot Integer
# easy
# https://leetcode.com/problems/find-the-pivot-integer

class Solution:
    def pivotInteger(self, n: int) -> int:
        left = left_sum = 1
        right = right_sum = n
        while left <= right:
            if left == right:
                return left if left_sum == right_sum else -1
            if left_sum <= right_sum:
                left += 1
                left_sum += left
            else:
                right -= 1
                right_sum += right
        return -1