# 2610. Convert an Array Into a 2D Array With Conditions
# medium
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        countMap = collections.defaultdict(int)
        for num in nums:
            countMap[num] += 1
        res = []
        for (num, count) in countMap.items():
            for i in range(count):
                if len(res) <= i:
                    res.append([])
                res[i].append(num)
        return res