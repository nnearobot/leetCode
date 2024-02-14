# 2149. Rearrange Array Elements by Sign
# medium
# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                res[pos] = num
                pos += 2
            else:
                res[neg] = num
                neg += 2

        return res
