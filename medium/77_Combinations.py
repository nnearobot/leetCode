# 77. Combinations
# Medium
# https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backTrack(first, arr):
            if len(arr) == k:
                res.append(arr[:])

            for i in range(first, n + 1):
                arr.append(i)
                backTrack(i + 1, arr)
                arr.pop()
            
        backTrack(1, [])
        return res