# 1160. Find Words That Can Be Formed by Characters
# easy
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

import collections

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charMap = collections.defaultdict(int)
        for char in chars:
            charMap[char] += 1

        sum_of_letters = 0
        for word in words:
            tmpMap = charMap.copy()
            make_sum = True
            for letter in word:
                if letter not in tmpMap or tmpMap[letter] < 1:
                    make_sum = False
                    break
                else:
                    tmpMap[letter] -= 1
            if make_sum:
                sum_of_letters += len(word)

        return sum_of_letters
