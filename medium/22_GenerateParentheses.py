# 22. Generate Parentheses
# medium
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def build_list(prev: str, pairs: int, stack: int) -> List[str]:
            nonlocal n

            if pairs == n and stack == 0:
                return [prev]

            res_1 = build_list(prev + "(", pairs + 1, stack + 1) if pairs < n else []
            res_2 = build_list(prev + ")", pairs, stack - 1) if pairs > 0 and stack > 0 else []

            return res_1 + res_2

        return build_list("(", 1, 1)