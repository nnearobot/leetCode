"""
167. Two Sum II - Input Array Is Sorted
Medium
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numMap:
                return [numMap[diff] + 1, i + 1]
            numMap[numbers[i]] = i
        return []