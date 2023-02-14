# 46. Permutations
# Medium
# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backTrack(first, arr):
            if len(arr) == n:
                res.append(arr[:])
                return

            for i in range(n):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    backTrack(i + 1, arr)
                    arr.pop()

        backTrack(0, [])
        
        return res