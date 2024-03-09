# 3005. Count Elements With Maximum Frequency
# easy
# https://leetcode.com/problems/count-elements-with-maximum-frequency

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = collections.Counter(nums)
        max_freq = max(freqs.values())
        return sum(filter(lambda x: x == max_freq, freqs.values()))