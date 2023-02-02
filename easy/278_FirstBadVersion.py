# 278. First Bad Version
# Easy
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        if isBadVersion(1):
            return 1
        if n == 2:
            return 2
        s = 1
        e = n
        minBad = 2
        while e > s + 1:
            n = math.ceil((e - s) / 2) + s
            if isBadVersion(n):
                e = n
            else:
                s = n
                minBad = n + 1
        return minBad