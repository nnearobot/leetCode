# 905. Sort Array By Parity
# easy
# https://leetcode.com/problems/sort-array-by-parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        '''
        # memory save:
        res = nums
        for i, num in enumerate(res):
            if num % 2 != 0:
                continue
            j = i
            while j > 0 and res[j - 1] % 2 != 0:
                res[j], res[j - 1] = res[j - 1], res[j]
                j -= 1
        return res
        '''

        # time (and also memory) save:
        even = [];
        odd = [];
        for i, num in enumerate(nums):
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return even + odd
