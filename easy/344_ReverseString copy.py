# 557. Reverse Words in a String III
# Easy
# https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseString(s: str) -> str:
            res = ""
            for i in range(len(s) - 1, -1, -1):
                res += s[i]
            return res
        words = s.split(" ")
        for i in range(len(words)):
            words[i] = reverseString(words[i])
        return " ".join(words)