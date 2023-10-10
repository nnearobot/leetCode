# 34. Find First and Last Position of Element in Sorted Array
# medium
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.findBinary(nums, target, True)
        end   = self.findBinary(nums, target, False)
        return [start, end]


    def findBinary(self, nums: List[int], target: int, start: bool) -> int:
        n = len(nums)
        if n == 0:
            return -1

        left = 0
        right = n - 1

        res = -1
        while left <= right:
            if left == right:
                return left if nums[left] == target else res

            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                res = mid
                if start:
                    right = mid - 1
                else:
                    left = mid + 1
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1

        return res
