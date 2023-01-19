"""
974. Subarray Sums Divisible by K
Medium
https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSumRemCount = {}
        summ = 0
        res = 0
        for i, n in enumerate(nums):
            summ += n
            rem = summ % k
            if rem in prefixSumRemCount:
                res += prefixSumRemCount[rem]
            else:
                prefixSumRemCount[rem] = 0
            prefixSumRemCount[rem] += 1
            if rem == 0:
                res += 1

        return res

"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSumRemCount = {}
        summ = 0
        for i, n in enumerate(nums):
            summ += n
            rem = summ % k
            if rem not in prefixSumRemCount:
                prefixSumRemCount[rem] = 0
            prefixSumRemCount[rem] += 1

        res = 0
        for rem in prefixSumRemCount:
            count = prefixSumRemCount[rem]
            if rem == 0:
                res += count
            if count == 2:
                res += 1
            if count > 2:
                res = res + (count - 1) * count // 2

        return res
"""