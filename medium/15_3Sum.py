# 15. 3Sum
# medium
# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, num1 in enumerate(nums):
            if num1 in dups:
                continue
            dups.add(num1)
            for j, num2 in enumerate(nums[i + 1:]):
                needed_summ = 0 - num1 - num2
                if needed_summ in seen and seen[needed_summ] == i:
                    res.add(tuple(sorted([num1, num2, needed_summ])))
                seen[num2] = i

        return res