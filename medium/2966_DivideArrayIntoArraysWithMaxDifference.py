# 2966. Divide Array Into Arrays With Max Difference
# medium
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for num in nums:
            if len(res) == 0 or len(res[-1]) == 3:
                res.append([num])
            else:
                if abs(res[-1][0] - num) <= k:
                    res[-1].append(num)
                else:
                    return []
        return res