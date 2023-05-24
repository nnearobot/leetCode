# 322. Coin Change
# Medium
# https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for value in coins:
                if i < value:
                    continue
                dp[i] = min(dp[i], dp[i - value] + 1)
        
        return dp[amount] if dp[amount] < amount + 1 else -1