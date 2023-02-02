# 953. Verifying an Alien Dictionary
# Easy
# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabetMap = {value: key for key, value in enumerate(order)}
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if alphabetMap[words[i + 1][j]] < alphabetMap[words[i][j]]:
                    return False
                if alphabetMap[words[i + 1][j]] > alphabetMap[words[i][j]]:
                    break
            if words[i + 1][j] == words[i][j] and len(words[i + 1]) < len(words[i]):
                return False
        return True