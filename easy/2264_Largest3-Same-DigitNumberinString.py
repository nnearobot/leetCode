# 2264. Largest 3-Same-Digit Number in String
# easy
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = -1
        for i in range(1, len(num) - 1):
            if num[i - 1] == num[i] and num[i + 1] == num[i]:
                max_good = max(max_good, int(num[i - 1:i + 2]))
                if num[i] == 9:
                    return '999'
        if max_good == -1:
            return ''
        return str(max_good) if max_good > 0 else '000'

        '''
        max_good = -1
        substring = ''
        for char in num:
            substr_len = len(substring)
            if substr_len == 0 or substring[0] != char:
                substring = char
                continue

            if substr_len < 3:
                substring += char
            if substr_len == 2:
                max_good = max(max_good, int(substring))
            
        if max_good == -1:
            return ''

        return str(max_good) if max_good > 0 else '000'
        '''
