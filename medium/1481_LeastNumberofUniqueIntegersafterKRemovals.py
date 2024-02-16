# 1481. Least Number of Unique Integers after K Removals
# medium
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_map = collections.defaultdict(int)
        for num in arr:
            num_map[num] += 1
        num_map = sorted(num_map.items(), key=lambda x: x[1])
        res = 0
        for val in num_map:
            if k == 0:
                res += 1
            elif k >= val[1]:
                k -= val[1]
            else:
                res += 1
                k = 0
        return res
