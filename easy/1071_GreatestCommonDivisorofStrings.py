# 1071. Greatest Common Divisor of Strings
# Easy
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0] != str2[0]:
            return ""
        
        a = len(str1)
        b = len(str2)
        
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        
        gcm = a + b

        res = ""
        for i in range(gcm):
            if str1[i] == str2[i]:
                res += str1[i]
            else:
                break
        
        if res * (len(str1) // gcm) == str1 and res * (len(str2) // gcm) == str2:
            return res
        
        return ""