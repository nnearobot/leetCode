# 88. Merge Sorted Array
# Easy
# https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p2 >= 0:
            num1 = nums1[p1] if p1 >= 0 else -10000000000
            num2 = nums2[p2]
            if num1 > num2:
                nums1[p] = num1
                p1 -= 1
            else:
                nums1[p] = num2
                p2 -=1
            p -= 1
