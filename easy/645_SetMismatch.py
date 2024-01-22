# 645. Set Mismatch
# easy
# https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        num_map = [0 for i in range(n)]
        res = [0, 0]
        for num in nums:
            num_map[num] += 1
            if num_map[num] == 2:
                res[0] = num
        for i in range(1, n):
            if num_map[i] == 0:
                res[1] = i
                break
        return res
