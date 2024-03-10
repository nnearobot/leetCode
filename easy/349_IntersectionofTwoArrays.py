# 349. Intersection of Two Arrays
# easy
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = collections.Counter(nums1)
        res = set()
        for num in nums2:
            if num in nums1_map:
                res.add(num)
        return list(res)