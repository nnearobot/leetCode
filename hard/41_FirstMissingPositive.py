# 41. First Missing Positive
# hard
# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_el = 1
        num_map = set()
        for num in nums:
            num_map.add(num)
            if num == min_el:
                while min_el in num_map:
                    min_el += 1
        return min_el