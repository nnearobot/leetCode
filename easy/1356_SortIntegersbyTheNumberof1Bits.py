# 1356. Sort Integers by The Number of 1 Bits
# Easy
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda num: (self.find_set_bit_count(num), num))
        return arr

    def find_set_bit_count(self, num):
        set_bits = 0
        while num:
            set_bits += 1
            num &= (num - 1)
        return set_bits

