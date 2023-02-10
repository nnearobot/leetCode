"""
55. Jump Game
Medium
https://leetcode.com/problems/jump-game/

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        memo = {}
        def dp(num) -> bool:
            if num not in memo:
                for step in range(min(nums[num], len(nums) - num - 1), 0, -1):
                    nextNum = num + step
                    if nextNum == len(nums) - 1:
                        memo[num] = True
                    elif nums[nextNum] == 0:
                        memo[num] = False
                    else:
                        memo[num] = dp(nextNum)
            return memo[num]
        
        res = dp(0)
        print(memo)
        
        return res