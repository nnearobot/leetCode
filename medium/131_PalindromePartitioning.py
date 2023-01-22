"""
131. Palindrome Partitioning
Medium
https://leetcode.com/problems/palindrome-partitioning/description/

"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]

        res = []
        partitions = []

        def backtrack(i, substring) -> None:
            if i == len(s):
                if len(partitions) > 0 and len(substring) == 0:
                    res.append(partitions[:])
                return
            
            substring += s[i]

            # move on with the next letter
            backtrack(i + 1, substring)

            # make a part
            if isPalindrome(substring):
                partitions.append(substring)
                backtrack(i + 1, "")
                partitions.pop()

        def isPalindrome(substring) -> bool:
            if len(substring) == 1:
                return True
            for i in range(len(substring) // 2):
                if substring[i] != substring[len(substring) - i - 1]:
                    return False
            return True 

        backtrack(0, "")

        return res
