# 2962. Count Subarrays Where Max Element Appears at Least K Times
# medium
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = right = 0
        n = len(nums)
        max_num = max(nums)
        max_num_count = 0
        res = 0
        while right < n:
            if nums[right] == max_num:
                max_num_count += 1
            if max_num_count == k:
                res += n - right
                while left <= right and max_num_count == k:
                    if nums[left] == max_num:
                        max_num_count -= 1
                    else:
                        res += n - right
                    left += 1
            right += 1
        return res