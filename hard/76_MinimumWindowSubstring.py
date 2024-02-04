# 76. Minimum Window Substring
# hard
# https://leetcode.com/problems/minimum-window-substring/description

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        counter = start = end = 0
        t_map = Counter(t)
        while start < len(s) and end < len(s):
            if s[end] in t_map:
                t_map[s[end]] -= 1
                if t_map[s[end]] >= 0:
                    counter += 1
                if counter == len(t):
                    while start <= end:
                        if s[start] in t_map:
                            if t_map[s[start]] < 0:
                                t_map[s[start]] += 1
                            else:
                                break
                        start +=1
                    if res == "" or end - start + 1 < len(res):
                        res = s[start:end + 1]
            end += 1
        return res