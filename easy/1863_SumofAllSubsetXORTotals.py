# 1863. Sum of All Subset XOR Totals
# easy
# https://leetcode.com/problems/sum-of-all-subset-xor-totals

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def subset_xor_sum(nums, rang) -> int:
            n = len(nums)
            if n == 1:
                return nums[0]

            summ = nums[0]
            for i in range(1, n):
                summ ^= nums[i]

            for i in range(rang, n):
                summ += subset_xor_sum(nums[:i] + nums[i + 1:], i)

            return summ

        return subset_xor_sum(nums, 0)