# 2125. Number of Laser Beams in a Bank
# medium
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        for row in bank:
            arr = [int(x) for x in row]
            devices = sum(arr)
            if devices > 0:
                if prev > 0:
                    res += devices * prev
                prev = devices
        return res