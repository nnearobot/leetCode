# 4. Median of Two Sorted Arrays
# Hard
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        center = math.ceil((m + n) / 2)
        p1, p2 = 0, 0

        def get_smaller():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p1 == m:
                ans = nums2[p2]
                p2 += 1
            else:
                ans = nums1[p1]
                p1 += 1
            return ans