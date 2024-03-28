# 2958. Length of Longest Subarray With at Most K Frequency
# medium
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = right = 0
        n = len(nums)
        num_freq = collections.defaultdict(int)
        max_length = 0
        while right < n:
            num_freq[nums[right]] += 1
            if num_freq[nums[right]] > k:
                max_length = max(max_length, right - left)
                while left < right:
                    num_freq[nums[left]] -= 1
                    left += 1
                    if nums[left - 1] == nums[right]:
                        break
            right += 1
        max_length = max(max_length, right - left)
        return max_length