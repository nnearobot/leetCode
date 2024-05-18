# 215. Kth Largest Element in an Array
# medium
# https://leetcode.com/problems/kth-largest-element-in-an-array

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        for i in range(k):
            el = heapq.heappop(maxHeap)
        return -el