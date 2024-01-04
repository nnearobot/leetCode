# 2870. Minimum Number of Operations to Make Array Empty
# medium
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_count = collections.defaultdict(int)
        for num in nums:
            num_count[num] += 1
        res = 0
        for count in num_count.values():
            if count == 1:
                return -1
            res += count // 3
            if count % 3 != 0:
                res += 1
        return res