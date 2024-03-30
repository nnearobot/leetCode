# 992. Subarrays with K Different Integers
# hard
# https://leetcode.com/problems/subarrays-with-k-different-integers

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        nums_count = collections.defaultdict(int)
        total_count = 0
        left = 0
        right = 0
        curr_count = 0
        n = len(nums)
        while right < n:
            nums_count[nums[right]] += 1
            if nums_count[nums[right]] == 1:
                k -= 1
            if k < 0:
                nums_count[nums[left]] -= 1
                if nums_count[nums[left]] == 0:
                    k += 1
                left += 1
                curr_count = 0
            if k == 0:
                while nums_count[nums[left]] > 1:
                    nums_count[nums[left]] -= 1
                    left += 1
                    curr_count += 1
                total_count += (curr_count + 1)
            right += 1
        return total_count