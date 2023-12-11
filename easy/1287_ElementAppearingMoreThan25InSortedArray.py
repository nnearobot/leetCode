# 1287. Element Appearing More Than 25% In Sorted Array
# easy
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        min_count = n // 4
        for i in range(n - min_count):
            if arr[i] == arr[i + min_count]:
                return arr[i]
        return -1