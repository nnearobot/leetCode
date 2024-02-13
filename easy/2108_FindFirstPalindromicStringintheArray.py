# 2108. Find First Palindromic String in the Array
# easy
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/


class Solution:
    def isPalindrom(self, word: str) -> bool:
        n = len(word)
        for i in range(n // 2):
            if word[i] != word[n - i - 1]:
                return False
        return True
        
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrom(word):
                return word
        return ""
 