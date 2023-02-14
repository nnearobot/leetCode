# 784. Letter Case Permutation
# Medium
# https://leetcode.com/problems/letter-case-permutation

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        digits = [str(i) for i in range(10)]

        def backTrack(i, str):
            if i == len(s):
                res.append(str)
                return
            
            if s[i] in digits:
                str += s[i]
            else:
                str += s[i].lower()
                backTrack(i + 1, str)
                str = str[:-1]
                str += s[i].upper()

            backTrack(i + 1, str)
            str = str[:-1]
        
        backTrack(0, "")

        return res
            