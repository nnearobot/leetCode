"""
491. Non-decreasing Subsequences
Medium
https://leetcode.com/problems/non-decreasing-subsequences/description/

"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subsequence = []

        def backtrack(i):
            if len(subsequence) > 1:
                res.add(tuple(subsequence))
            if i == len(nums):
                return
            if not subsequence or nums[i] >= subsequence[-1]:
                subsequence.append(nums[i])
                backtrack(i + 1)
                subsequence.pop()
            backtrack(i + 1)
                
        backtrack(0)

        return res