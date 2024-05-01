# 2000. Reverse Prefix of Word
# easy
# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = [w for w in word]
        for i, w in enumerate(word):
            if w == ch:
                for j in range((i + 1) // 2):
                    arr[j], arr[i - j] = arr[i - j], arr[j]
                break
        return "".join(arr)