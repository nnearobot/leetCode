# 629. K Inverse Pairs Array
# hard
# https://leetcode.com/problems/k-inverse-pairs-array/

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0 for _ in range(k + 1)]
        MOD = 10**9 + 7
        for i in range(1, n + 1):
            tmp = [0 for _ in range(k + 1)]
            tmp[0] = 1
            for j in range(1, k + 1):
                val = dp[j - i] if j >= i else 0
                val = dp[j] + MOD - val
                val = val % MOD
                tmp[j] = (tmp[j - 1] + val) % MOD
            dp = tmp
        val = dp[k - 1] if k > 0 else 0
        return (dp[k] + MOD - val) % MOD
