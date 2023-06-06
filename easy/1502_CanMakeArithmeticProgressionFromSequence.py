# 1502. Can Make Arithmetic Progression From Sequence
# Easy
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        step = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != step:
                return False

        return True
