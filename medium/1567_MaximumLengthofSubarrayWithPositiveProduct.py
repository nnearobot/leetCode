"""
1567. Maximum Length of Subarray With Positive Product
Medium
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/description

"""

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        n = len(nums)
        dp = [[0, 0] for _ in range(n)]

        if nums[0] > 0:
            dp[0][0] = 1

        if nums[0] < 0:
            dp[0][1] = 1

        res = dp[0][0]

        for i, num in enumerate(nums):
            if i == 0:
                continue
            if num > 0:
                dp[i][0] = dp[i - 1][0] + 1
                if dp[i - 1][1] > 0:
                    dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1)
            if num < 0:
                dp[i][1] = dp[i - 1][0] + 1
                if dp[i - 1][1] > 0:
                    dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)

            res = max(res, dp[i][0])

        return res

