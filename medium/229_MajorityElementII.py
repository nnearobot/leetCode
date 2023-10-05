# 229. Majority Element II
# Medium
# https://leetcode.com/problems/majority-element-ii


from collections import defaultdict, List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        res = []
        for num in hashMap:
            if hashMap[num] > n:
                res.append(num)
        return res
        