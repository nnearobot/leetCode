# 20. Valid Parentheses
# Easy
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        opens = ['(', '{', '[']
        closes = [')', '}', ']']
        stack = []
        for c in s:
            if c in opens:
                stack.append(c)
            elif c in closes:
                if len(stack) == 0:
                    return False
                cc = stack.pop()
                if opens.index(cc) != closes.index(c):
                    return False
        return len(stack) == 0
