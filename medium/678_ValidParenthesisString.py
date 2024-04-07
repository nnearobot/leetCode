# 678. Valid Parenthesis String
# medium
# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_brackets = []
        stack_asterisks = []
        for i, char in enumerate(s):
            if char == '(':
                stack_brackets.append(i)
            elif char == '*':
                stack_asterisks.append(i)
            else:
                if len(stack_brackets):
                    stack_brackets.pop()
                elif len(stack_asterisks):
                    stack_asterisks.pop()
                else:
                    return False
        while len(stack_brackets) > 0 and len(stack_asterisks) > 0:
            bracket = stack_brackets.pop()
            asterisk = stack_asterisks.pop()
            if bracket > asterisk:
                return False
        return len(stack_brackets) == 0