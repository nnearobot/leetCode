# 451. Sort Characters By Frequency
# medium
# https://leetcode.com/problems/sort-characters-by-frequency


class Solution:
    def frequencySort(self, s: str) -> str:
        str_map = collections.defaultdict(int) 
        for l in s:
            str_map[l] += 1
        str_map = sorted(str_map.items(), key=lambda x: x[1], reverse=True)
        res = ""
        for (l, count) in str_map:
            res += l * count
        return res